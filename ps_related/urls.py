from django.urls import path
from .views import books_in_stock


urlpatterns = [
    path('books/in-stock/', books_in_stock, name='in_stock_books'),
]
