from django.db import models
from django.conf import settings
from django.utils.text import slugify

class EventCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class EventType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name



class Event(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)
    posted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posted_events'
    )
    is_organizer = models.BooleanField(default=False)
    organizer_name = models.CharField(max_length=100, blank=True)

    category = models.ForeignKey(EventCategory, on_delete=models.SET_NULL, null=True)
    event_type = models.ForeignKey(EventType, on_delete=models.SET_NULL, null=True)
    genres = models.ManyToManyField(Genre, related_name='events')

    date = models.DateTimeField()
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            num = 1
            while Event.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{num}"
                num += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

