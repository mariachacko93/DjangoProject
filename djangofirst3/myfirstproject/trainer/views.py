from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def trainerRegistration(request):
    return render(request,"trainer/trainerreg.html")

def trainerlogin(request):
    return render(request,"trainer/trainerlogin.html")

