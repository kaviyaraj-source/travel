from django.contrib import admin

from .models import Destination, Testimonial, TourPackage, TravelInquiry


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'price_from', 'rating', 'is_featured')
    list_filter = ('country', 'is_featured')
    search_fields = ('name', 'country')


@admin.register(TourPackage)
class TourPackageAdmin(admin.ModelAdmin):
    list_display = ('title', 'destination', 'duration_days', 'price', 'is_popular')
    list_filter = ('difficulty', 'is_popular', 'destination')
    search_fields = ('title', 'destination__name')


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'rating', 'is_active')
    list_filter = ('is_active', 'rating')


@admin.register(TravelInquiry)
class TravelInquiryAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'destination_interest', 'travelers', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('full_name', 'email', 'destination_interest')
    readonly_fields = ('created_at',)
