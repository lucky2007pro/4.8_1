from django.shortcuts import render

from books.models import Book


# Create your views here.

def books(request):
    books = Book.objects.all()
    return render(request, 'books.html', {'books': books})