from django.shortcuts import render
from .models import Book


def books_in_stock(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'books_in_stock.html', context)
