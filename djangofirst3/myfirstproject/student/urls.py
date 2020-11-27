
# from django.contrib import admin

from django.urls import path
from student.views import studRegistration,studlogin,regStudDetails,logstuddetails,addnum,add


urlpatterns = [
    path("studregistration",studRegistration,name="studreg"),
    path("studlogin",studlogin, name="studlogin"),
    path("register",regStudDetails, name="register"),
    path("login",logstuddetails,name="login"),
    path("add",add,name="add"),
    path("addnum",addnum,name="addnum"),

]
