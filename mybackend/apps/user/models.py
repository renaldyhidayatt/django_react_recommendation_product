from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import MyUserManager
from apps.shared.models import TimeStampedModel


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin, TimeStampedModel):
    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    is_staff = models.BooleanField(
        default=False,
        help_text=("Designates whether the user can log into this admin site."),
    )
    reviews = models.ManyToManyField("review.Review", related_name="user_reviews")
    carts = models.ManyToManyField("cart.Cart", related_name="user_carts")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = MyUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.email
