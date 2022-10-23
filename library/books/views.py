from django.http import HttpResponse
from .models import Book
from django.template import loader
from django.shortcuts import render,get_object_or_404

def index(request):
    return HttpResponse("Library")

def book_info(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'books/detail.html', {'book' : book})

def book_list(request):
    latest_books_list = Book.objects.order_by('-date_published')[:5]
    context = {'latest_books_list' : latest_books_list}
    return render(request, 'books/index.html', context)
