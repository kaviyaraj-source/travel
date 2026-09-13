from django.db import models


class Destination(models.Model):
    name = models.CharField(max_length=120)
    country = models.CharField(max_length=80)
    tagline = models.CharField(max_length=200)
    description = models.TextField()
    image_url = models.URLField(max_length=500)
    price_from = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=4.5)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-is_featured', 'name']

    def __str__(self):
        return f'{self.name}, {self.country}'


class TourPackage(models.Model):
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('moderate', 'Moderate'),
        ('challenging', 'Challenging'),
    ]

    title = models.CharField(max_length=150)
    destination = models.ForeignKey(
        Destination, on_delete=models.CASCADE, related_name='packages'
    )
    duration_days = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES, default='easy')
    highlights = models.TextField(help_text='Comma-separated highlights')
    image_url = models.URLField(max_length=500)
    is_popular = models.BooleanField(default=False)

    class Meta:
        ordering = ['-is_popular', 'title']

    def __str__(self):
        return self.title

    @property
    def highlights_list(self):
        return [h.strip() for h in self.highlights.split(',') if h.strip()]


class Testimonial(models.Model):
    author_name = models.CharField(max_length=100)
    author_role = models.CharField(max_length=120, blank=True)
    content = models.TextField()
    rating = models.PositiveSmallIntegerField(default=5)
    avatar_url = models.URLField(max_length=500, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.author_name


class TravelInquiry(models.Model):
    full_name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    destination_interest = models.CharField(max_length=150, blank=True)
    travel_date = models.DateField(null=True, blank=True)
    travelers = models.PositiveIntegerField(default=1)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Travel inquiries'

    def __str__(self):
        return f'{self.full_name} — {self.email}'
