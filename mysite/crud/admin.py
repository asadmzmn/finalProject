# from termios import OFILL
from django.contrib import admin
from .models import Experience, Office, Education, ImageGallery

# Register your models here.

admin.site.register(Office)

admin.site.register(Experience)

admin.site.register(Education)

admin.site.register(ImageGallery)

