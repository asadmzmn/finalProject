from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.


def loginPage(request):
    return render(request, 'html/login.html')

def registerPage(request):
    if request.method == "GET":
        return render(request, 'html/register.html')
    elif request.method == "POST":
        # print(request.POST)
        userName = request.POST["user_name"]
        password = request.POST["password"]
        firstName = request.POST["first_name"]
        lastName = request.POST["last_name"]
        email = request.POST["email"]
        
        try:
            User.objects.create_user(username = userName, password=password, email=email, first_name=firstName, last_name=lastName)
            messages.success(request, "User created succesfully")
            return redirect('loginpage')
        except Exception as e:
            messages.error(request, "Can't create user" + str(e))
            return redirect("registerpage")


