from email.policy import default
from django.db import models

# Create your models here.


class Office(models.Model):
    company_name = models.CharField(max_length=1000)
    designation = models.CharField(max_length=1000)
    img_up = models.ImageField(upload_to = 'images/', default="")


class Experience(models.Model):
    duration = models.CharField(max_length=1000)
    post = models.CharField(max_length=1000)
    experience = models.CharField(max_length=1000)
    address = models.CharField(max_length=1000)


class Education(models.Model):
    duration = models.CharField(max_length=1000)
    institute = models.CharField(max_length=1000)
    tagline = models.CharField(max_length=1000)
    address = models.CharField(max_length=1000)

class ImageGallery(models.Model):
    img_up = models.ImageField(upload_to = 'gallery/', default="")
    caption = models.CharField(max_length=10000)

