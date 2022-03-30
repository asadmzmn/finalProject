from django.urls import path
from .views import blogPage


urlpatterns = [
    path("allblogs/", blogPage, name="allblog")
]