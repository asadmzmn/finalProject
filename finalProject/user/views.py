from django.shortcuts import render

# Create your views here.


def loginPage(request):
    return render(request, 'html/login.html')

def registerPage(request):
    return render(request, 'html/register.html')