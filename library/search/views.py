# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import BookDetail, Book
from difflib import SequenceMatcher

# Create your views here.


def search_books(request):
    context = {}

    if request.method == 'POST':
        try:
            search_by = request.POST.get('search_by', False)
            search_field = request.POST.get('search_field', False)
            # books = BookDetail.objects.all()
            # books_list = []
            
            # for book in books:
            #     if SequenceMatcher(None, book.return_field(search_by), search_field).ratio() > 0.25:
            #         print book.return_field(search_by)
            #         books_list.append(book)
            search_by += "__contains" 
            books_list = BookDetail.objects.filter(**{search_by: search_field})
            context['books_list'] = books_list
        except UnboundLocalError:
            pass

    return render(request, 'search/search_book.html', context)


def list_books(request, book_id):
    context = {}

    book_detail = BookDetail.objects.get(id=book_id)
    context['book_detail'] = book_detail

    books = Book.objects.filter(book_id=book_id)
    context['books'] = books

    return render(request, 'search/list_books.html', context)
