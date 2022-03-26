from django.shortcuts import redirect, render
from .models import Education, Office, Experience, ImageGallery

# Create your views here.


def resumePage(request):
    context ={ 
        'education': [
      
    {
        "duration": "JANUARY 2003 - JANUARY 2004",
        "institute": "Primary Institute",
        "tagline": "People only remember the First and forget the Rest",
        "address": "Nou-Bahini Institute, Dhaka"
    },
      
    {
        "duration": "FEBRUARY 2004- DECEMBER 2006 \nFEBRUARY 2011- MARCH 2014",
        "institute": "Primary & Secondary institute",
        "tagline": "The Golden moment of my Life",
        "address": "Nou-Bahini Institute, Chittagong" 
    },
        {
        "duration": "July 2014 - May 2016",
        "institute": "Higher Secondary",
        "tagline": "Game changing period",
        "address": "Bangladesh Navy College, Chittagong" 
    },
            {
        "duration": "January 2017 - July 2021 ",
        "institute": "Bachelor of Science in SOFTWARE ENGINNERING",
        "tagline": "Seriously thinking about life",
        "address": "Daffodil International University" 
    },
    
    ],
        "experience": [
              {
        "duration": "OCTOBER 2021 - PRESENT",
        "post": "Software Development Engineer",
        "experience": "Reactjs , Python, Django",
        "address": "Datasoft Systems Bangladesh, LTD" 
    },
    {
        "duration": "FEBRUARY 2021 - SEPTEMBER 2021",
        "post": "Full-stack Web Developer",
        "experience": "Nodejs, Reactjs, AWS",
        "address": "Doodle Technologies" 
    },
        {
        "duration": "OCTOBER 2020 - FEBRUARY 2021",
        "post": "Backend Developer",
        "experience": "Golang, Gin, PostgreSQL",
        "address": "Upskill" 
    }
  
    ],
    "contact_details": [
    {
        "email":"mahidulmoon@gmail.com",
        "phone":"+8801771042196",
        "address":"YounusKhans's scholar's Garden \nAshulia \nSavar, Dhaka"
    }
    ]
    
    }
    return render(request, 'resume_boot_2.html', context)


def anotherPage(request):
    return render(request, 'another.html')




def experienceShow(request):
    qs1 = Education.objects.all()
    qs2 = Experience.objects.all()
    # context={
    #     "data":queryset
    # }
    context={
    
        'education': qs1,
    
        "experience": qs2,


    "contact_details": [
    {
        "email":"mahidulmoon@gmail.com",
        "phone":"+8801771042196",
        "address":"YounusKhans's scholar's Garden \nAshulia \nSavar, Dhaka"
    }
    ]
    
    }
    return render(request, "experience.html", context)


# new function to get the user input
def fromUserInput(request):
    # print(request.method)
    if request.method =="GET":
        return render(request, "form_user_input.html")

    # elif request.method == "POST":
    #     company_user_input = request.POST["company_input"]
    #     designation_user_input = request.POST["designation_input"]
    #     # queryset = Office.objects.create(company_name=company_user_input, designation=designation_user_input)

    #     new_data = Office(company_name=company_user_input, designation=designation_user_input)
    #     new_data.save()
    #     return render(request, "dbDataShow.html", new_data)


def dbDataShow(request):

    if request.method =="GET":
        queryset = Office.objects.all()
        context={
                "data":queryset
            }
        return render(request, "dbDataShow.html", context)
    elif request.method == "POST":
        company_user_input = request.POST["company_input"]
        designation_user_input = request.POST["designation_input"]
        image = request.FILES["photo"]
        Office.objects.create(company_name=company_user_input, designation=designation_user_input, img_up=image)

        queryset = Office.objects.all()
        context={
                "data":queryset
            }
        return render(request, "dbDataShow.html", context)

def updateDelete(request, pk):
    if request.method =="GET":

        # exactData = get_object_or_404
        exactData = Office.objects.get(id=pk)
        context = {
            "data": exactData
        }
        
        return render(request, "updateTemplate.html", context)

    else:
        # print("inside updat view:", request.POST)
        exactData = Office.objects.get(id=pk)
        company=request.POST["company_input"]
        designation=request.POST["designation_input"]

        exactData.company_name=company
        exactData.designation = designation
        exactData.save()
        return redirect('dbData')

def deleteObj(request, sk):

    exactData = Office.objects.get(id=sk)
    exactData.delete()
    return redirect('dbData')


def imageGallery(request):
    # print(request.method)
    if request.method =="GET":
        queryset = Office.objects.all()
        context={
                "data":queryset
            }
        return render(request, "gallery.html", context)
    elif request.method == "POST":
        photo_caption = request.POST["image_caption"]
        image = request.FILES["photo"]
        ImageGallery.objects.create(caption=photo_caption, img_up=image)

        queryset = ImageGallery.objects.all()
        context={
                "data":queryset
            }
        return render(request, "gallery.html", context)