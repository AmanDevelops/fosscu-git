from django.db import models

# Create your models here.
def members():
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image_url = models.CharField(max_length=255)