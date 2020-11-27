from django.shortcuts import render,redirect
from django.http import HttpResponse
from books.models import Book
from books.forms import BookCreateForm
# Create your views here.

def createBook(request):
    form=BookCreateForm
    context={}
    context["form"]=form
    if(request.method=='POST'):
        form=BookCreateForm(request.POST)
        if(form.is_valid()):
            bookname =form.cleaned_data.get("bookname")
            price = form.cleaned_data.get("price")
            pages =form.cleaned_data.get("pages")
            author =form.cleaned_data.get("author")
            print(bookname, ",", price, ",", pages, ",", author)
            book = Book(book_name=bookname, price=price, pages=pages, author=author)
            book.save()
            return redirect("getbooks")
    return render(request,"books/bookcreate.html",context)


def getBooks(request):
    books=Book.objects.all()
    context={}
    context["books"]=books
    return render(request, "books/listbooks.html",context)



