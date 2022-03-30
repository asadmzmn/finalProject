from django.urls import path
from .views import logOut, loginPage, registerPage



urlpatterns = [
    path('', loginPage, name="loginpage"),
    path('register/', registerPage, name="registerpage"),
    path('logout/', logOut, name="logout"),


]