from django.db import models
from cloudinary_storage.storage import RawMediaCloudinaryStorage
from django.utils.text import slugify
from apps.shared.models import TimeStampedModel


# Create your models here.
class Category(TimeStampedModel):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=70)
    slug_category = models.CharField(max_length=70, null=True, blank=True)
    image_category = models.ImageField(upload_to="images/", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug_category = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
