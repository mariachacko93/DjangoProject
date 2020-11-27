from django.shortcuts import render,redirect
from django.http import HttpResponse
from person.models import Person

# Create your views here.
from person.forms import PersonCreateForm

def personPage(request):

    form=PersonCreateForm
    context={}
    context["form"]=form
    if request.method=="POST":
        form=PersonCreateForm(request.POST)
        if form.is_valid():
            personname = request.POST.get("personname")
            age = request.POST.get("age")
            salary = request.POST.get("salary")
            desig = request.POST.get("desig")
            print(personname, ",", age, ",", salary, ",", desig)
            person = Person(personname=personname, age=age, salary=salary, desig=desig)
            person.save()
            return redirect("getdetails")

    return render(request,"person/person.html",context)


def getDetails(request):
    person=Person.objects.all()
    context={}
    context["person"]=person
    return render(request,"person/personlist.html", context)
