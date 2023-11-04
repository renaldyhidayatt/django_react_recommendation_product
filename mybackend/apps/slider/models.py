from django.db import models
from apps.shared.models import TimeStampedModel


# Create your models here.
class Slider(TimeStampedModel):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/", blank=True)

    def __str__(self):
        return self.name
