from django.urls import path
from .views import loginPage, registerPage



urlpatterns = [
    path('', loginPage, name="loginpage"),
    path('register/', registerPage, name="registerpage")

]