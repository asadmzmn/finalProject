from django.shortcuts import render

# Create your views here.


def mainContent(request):
    return render(request, 'index.html')

def anotherContent(request):
    return render(request, 'another_2.html')