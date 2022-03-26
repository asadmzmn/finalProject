from cmath import exp
from django.urls import path
from .views import deleteObj, resumePage, anotherPage,dbDataShow, experienceShow, fromUserInput, updateDelete, deleteObj, imageGallery


urlpatterns = [
    path("resume/", resumePage, name= "resume_page"),
    path("another/", anotherPage, name= "another_page"),
    path("dbDataShow/", dbDataShow, name= "dbData"),
    path("experience/", experienceShow, name="experienceDb"),
    path("userInput/", fromUserInput, name="user_input"),
    path("updatedelete/<str:pk>/", updateDelete, name="update_delete"),
    path("delete/<str:sk>/", deleteObj, name="deleteData"),
    path("photogallery/", imageGallery, name="image_gallery")

]
