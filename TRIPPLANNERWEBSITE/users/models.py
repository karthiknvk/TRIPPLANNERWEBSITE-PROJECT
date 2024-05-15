from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    is_accommodation = models.BooleanField(default=False)
    user_image= models.ImageField(upload_to='user_images/', blank=True, null=True, default=None)

