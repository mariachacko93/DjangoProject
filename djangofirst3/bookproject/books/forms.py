from django import forms
class BookCreateForm(forms.Form):
    bookname=forms.CharField(max_length=120)
    price=forms.IntegerField()
    pages=forms.IntegerField()
    author=forms.CharField(max_length=120)