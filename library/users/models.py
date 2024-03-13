from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

ST = "Student"
AD = "Admin"
# SA = "Super-Admin"

ROLE_CHOICES = (
    (ST, "Student"),
    (AD, "Admin"),
    # (SA, "Super-Admin"),
)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("Email Address"), unique=True)
    first_name = models.CharField(max_length=50, default='default-firstname')
    last_name = models.CharField(max_length=50, default='default-lastname')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    profile_image = models.ImageField(upload_to='User-Profiles/', default='/defaults/no-profile.png')


    role = models.CharField(max_length=30, choices = ROLE_CHOICES, default='ST')


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

# Create your models here.
# class Admin(CustomUser, models.Model):
#     admin_id = models.IntegerField(primary_key=True)
