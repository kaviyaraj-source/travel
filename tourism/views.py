from django.db.models import Avg, Count
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from .models import Destination, Testimonial, TourPackage, TravelInquiry


def home(request):
    featured_destinations = Destination.objects.filter(is_featured=True)[:6]
    if not featured_destinations.exists():
        featured_destinations = Destination.objects.all()[:6]

    popular_packages = TourPackage.objects.filter(is_popular=True).select_related('destination')[:6]
    if not popular_packages.exists():
        popular_packages = TourPackage.objects.select_related('destination').all()[:6]

    testimonials = Testimonial.objects.filter(is_active=True)[:4]

    stats = {
        'destinations': Destination.objects.count(),
        'packages': TourPackage.objects.count(),
        'happy_travelers': TravelInquiry.objects.aggregate(total=Count('travelers'))['total'] or 0,
        'avg_rating': Testimonial.objects.filter(is_active=True).aggregate(avg=Avg('rating'))['avg'] or 4.8,
    }

    context = {
        'featured_destinations': featured_destinations,
        'popular_packages': popular_packages,
        'testimonials': testimonials,
        'stats': stats,
        'hero_destinations': Destination.objects.filter(is_featured=True)[:3],
    }
    return render(request, 'tourism/index.html', context)


@require_http_methods(['POST'])
def submit_inquiry(request):
    TravelInquiry.objects.create(
        full_name=request.POST.get('full_name', '').strip(),
        email=request.POST.get('email', '').strip(),
        phone=request.POST.get('phone', '').strip(),
        destination_interest=request.POST.get('destination_interest', '').strip(),
        travel_date=request.POST.get('travel_date') or None,
        travelers=int(request.POST.get('travelers') or 1),
        message=request.POST.get('message', '').strip(),
    )
    return redirect('/#contact?submitted=1')
