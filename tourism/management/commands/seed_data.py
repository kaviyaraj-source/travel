from django.core.management.base import BaseCommand

from tourism.models import Destination, Testimonial, TourPackage


class Command(BaseCommand):
    help = 'Seed the database with sample travel tourism data'

    def handle(self, *args, **options):
        if Destination.objects.exists():
            self.stdout.write(self.style.WARNING('Data already exists. Skipping seed.'))
            return

        destinations_data = [
            {
                'name': 'Santorini',
                'country': 'Greece',
                'tagline': 'Whitewashed cliffs & Aegean sunsets',
                'description': 'Experience iconic blue-domed churches, volcanic beaches, and world-famous sunsets over the caldera.',
                'image_url': 'https://images.unsplash.com/photo-1613395877344-13d4a8e0d49e?w=1200',
                'price_from': 1299.00,
                'rating': 4.9,
                'is_featured': True,
            },
            {
                'name': 'Bali',
                'country': 'Indonesia',
                'tagline': 'Temples, rice terraces & tropical bliss',
                'description': 'Discover lush jungles, sacred temples, and pristine beaches on the Island of the Gods.',
                'image_url': 'https://images.unsplash.com/photo-1537996194471-e657df975ab4?w=1200',
                'price_from': 899.00,
                'rating': 4.8,
                'is_featured': True,
            },
            {
                'name': 'Kyoto',
                'country': 'Japan',
                'tagline': 'Ancient culture meets serene beauty',
                'description': 'Walk through bamboo groves, visit golden temples, and witness timeless Japanese traditions.',
                'image_url': 'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?w=1200',
                'price_from': 1499.00,
                'rating': 4.9,
                'is_featured': True,
            },
            {
                'name': 'Swiss Alps',
                'country': 'Switzerland',
                'tagline': 'Alpine peaks & crystal lakes',
                'description': 'Ride scenic trains, hike mountain trails, and breathe in the crisp alpine air.',
                'image_url': 'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99?w=1200',
                'price_from': 1799.00,
                'rating': 4.7,
                'is_featured': True,
            },
            {
                'name': 'Maldives',
                'country': 'Maldives',
                'tagline': 'Overwater villas & turquoise lagoons',
                'description': 'Unwind in luxury overwater bungalows surrounded by coral reefs and crystal-clear waters.',
                'image_url': 'https://images.unsplash.com/photo-1514282401047-d79a71a590e8?w=1200',
                'price_from': 2199.00,
                'rating': 5.0,
                'is_featured': True,
            },
            {
                'name': 'Patagonia',
                'country': 'Argentina',
                'tagline': 'Wild frontiers at the end of the world',
                'description': 'Trek through dramatic glaciers, rugged peaks, and untouched wilderness in South America.',
                'image_url': 'https://images.unsplash.com/photo-1585409677983-0f6c41ca9ca3?w=1200',
                'price_from': 1899.00,
                'rating': 4.8,
                'is_featured': True,
            },
        ]

        destinations = {}
        for data in destinations_data:
            destinations[data['name']] = Destination.objects.create(**data)

        packages_data = [
            {
                'title': 'Aegean Dream Escape',
                'destination': destinations['Santorini'],
                'duration_days': 7,
                'price': 2499.00,
                'difficulty': 'easy',
                'highlights': 'Sunset cruise, Wine tasting, Caldera hike, Private villa stay',
                'image_url': 'https://images.unsplash.com/photo-1570077186670-aa1f791a1c6e?w=800',
                'is_popular': True,
            },
            {
                'title': 'Bali Wellness Retreat',
                'destination': destinations['Bali'],
                'duration_days': 10,
                'price': 1899.00,
                'difficulty': 'easy',
                'highlights': 'Yoga sessions, Ubud temples, Rice terrace trek, Spa treatments',
                'image_url': 'https://images.unsplash.com/photo-1559628233-100c798642d4?w=800',
                'is_popular': True,
            },
            {
                'title': 'Kyoto Cultural Journey',
                'destination': destinations['Kyoto'],
                'duration_days': 8,
                'price': 2799.00,
                'difficulty': 'moderate',
                'highlights': 'Tea ceremony, Geisha district, Bamboo forest, Bullet train',
                'image_url': 'https://images.unsplash.com/photo-1545569341-9eb8b30979d9?w=800',
                'is_popular': True,
            },
            {
                'title': 'Alpine Explorer',
                'destination': destinations['Swiss Alps'],
                'duration_days': 6,
                'price': 2299.00,
                'difficulty': 'moderate',
                'highlights': 'Glacier Express, Matterhorn views, Lake cruise, Mountain hiking',
                'image_url': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800',
                'is_popular': True,
            },
            {
                'title': 'Maldives Luxury Getaway',
                'destination': destinations['Maldives'],
                'duration_days': 5,
                'price': 3499.00,
                'difficulty': 'easy',
                'highlights': 'Overwater villa, Snorkeling, Private dining, Sunset fishing',
                'image_url': 'https://images.unsplash.com/photo-1573843981267-be1999ff37cd?w=800',
                'is_popular': True,
            },
            {
                'title': 'Patagonia Adventure Trek',
                'destination': destinations['Patagonia'],
                'duration_days': 12,
                'price': 3199.00,
                'difficulty': 'challenging',
                'highlights': 'Perito Moreno glacier, Torres del Paine, Wildlife safari, Camping',
                'image_url': 'https://images.unsplash.com/photo-1464822759844-d150baec0133?w=800',
                'is_popular': True,
            },
        ]

        for data in packages_data:
            TourPackage.objects.create(**data)

        testimonials_data = [
            {
                'author_name': 'Sarah Mitchell',
                'author_role': 'Travel Blogger',
                'content': 'Wanderlust Voyages crafted the most seamless trip of my life. Santorini at sunset was pure magic — every detail was perfectly planned.',
                'rating': 5,
                'avatar_url': 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=200',
            },
            {
                'author_name': 'James Chen',
                'author_role': 'Photographer',
                'content': 'The Kyoto cultural tour exceeded every expectation. Our guide was incredibly knowledgeable and the accommodations were stunning.',
                'rating': 5,
                'avatar_url': 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=200',
            },
            {
                'author_name': 'Elena Rodriguez',
                'author_role': 'Adventure Enthusiast',
                'content': 'Patagonia trek was challenging but absolutely worth it. The team handled logistics flawlessly while we focused on the adventure.',
                'rating': 5,
                'avatar_url': 'https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=200',
            },
            {
                'author_name': 'Michael Okafor',
                'author_role': 'Business Executive',
                'content': 'Maldives luxury package was the perfect anniversary gift. From booking to checkout, the service was world-class and personal.',
                'rating': 5,
                'avatar_url': 'https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=200',
            },
        ]

        for data in testimonials_data:
            Testimonial.objects.create(**data)

        self.stdout.write(self.style.SUCCESS(
            f'Seeded {len(destinations)} destinations, {len(packages_data)} packages, '
            f'and {len(testimonials_data)} testimonials.'
        ))
