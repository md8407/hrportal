
from django.contrib import admin
from django.urls import path,include
from employee import views


urlpatterns = [
   
    path('',views.homepage,name="index"),

    path('aboutus/',views.aboutus, name="aboutus"),
    path('contact/',views.contact, name="contact"),
    path('trending/',views.trend, name= "trending"),
    path('Explore work/',views.explore,name = "explorework"),
    # path('register/',)
    # path('register',RegisterView.as_view())
    

]