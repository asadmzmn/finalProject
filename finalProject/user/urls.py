from django.urls import path
from .views import loginPage
urlpatterns = [
    path('', loginPage, name="login_page")
]