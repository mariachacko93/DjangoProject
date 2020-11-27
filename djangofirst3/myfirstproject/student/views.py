from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#core functinalities
def studRegistration(request):
    # return HttpResponse("<h1>Welcome to Student Application</h1>")# only displays welcome we need complete registration
    return render(request,"student/studreg.html")

def studlogin(request):
    # return HttpResponse("<h1> welcome to login<h1>")
    print("hello")
    return render(request, "student/studlogin.html")

def regStudDetails(request):
    firstname=request.POST.get("firstname")
    lastname=request.POST.get("lastname")
    address=request.POST.get("address")
    gender=request.POST.get("gender")
    print(firstname,",",lastname,",",address,",",gender)

    return render(request,"student/studlogin.html")

def logstuddetails(request):
    username=request.POST.get("username")
    password=request.POST.get("password")
    print(username,",",password)

    context={}
    context["name"]=username
    context["password"]=password

    return render(request,"student/studenthome.html",context)

def add(request):
    return render(request,"student/add.html")

def addnum(request):
    num1=request.POST.get("num1")
    num2=request.POST.get("num2")
    res=int(num1)+int(num2)
    print(num1,",",num2,",",res)

    context={}
    context["num1"]=num1
    context["num2"]=num2
    context["res"]=res

    return render(request,"student/adddisplay.html",context)

