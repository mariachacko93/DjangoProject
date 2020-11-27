from django import forms

class PersonCreateForm(forms.Form):
    personname=forms.CharField(max_length=130)
    age=forms.IntegerField()
    salary=forms.IntegerField()
    desig=forms.CharField(max_length=130)