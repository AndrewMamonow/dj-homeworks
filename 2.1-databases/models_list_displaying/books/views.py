from django.shortcuts import render
from .models import Book
from django.core.paginator import Paginator
from django.utils import timezone
from datetime import datetime


def books_view(request):
    template = 'books/books_list.html'
    context = {}
    return render(request, template, context)

def book_list(request):
    template = 'books/books_list.html'
    books = Book.objects.all().order_by('-pub_date')
    context = {
        'pages': books
    } 
    return render(request, template, context)

def books_by_date(request, pub_date):
    template = 'books/books_by_date.html'
    books_objects = Book.objects.filter(pub_date=pub_date)
    paginator = Paginator(books_objects, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    books_next = (Book.objects.filter(pub_date__gt=pub_date).order_by('pub_date').first())
    if books_next:
        next_date = str(books_next.pub_date)
    else:
        next_date = None

    books_previous = Book.objects.filter(pub_date__lt=pub_date).order_by('pub_date').first()
    if books_previous:
        previous_date = str(books_previous.pub_date)
    else:
        previous_date = None
    context = {
        'books': page_obj,
        'next_date': next_date,
        'previous_date': previous_date,
    }
    return render(request, template, context)
    