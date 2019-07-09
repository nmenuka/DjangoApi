from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class User(AbstractUser):
    ROLES = (("SA", "SuperAdmin"),("NA", "NormalAdmin"),("JA", "Journalist"),("GU", "GuestUser"))
    role = models.CharField(choices=ROLES, max_length=2 , default="GU")
    email = models.EmailField(max_length=50, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username', 'password')

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    dob = models.DateField()
    address = models.CharField(max_length=30)
    display_image = models.ImageField(upload_to= "uploads", null=True)