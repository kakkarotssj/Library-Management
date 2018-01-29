# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import BookDetail, Book, Student, IssueDetail
# Register your models here.


class IssueDetailModelAdmin(admin.ModelAdmin):
    list_display = ["get_book_title", "get_student_id"]


class StudentModelAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "user_id", "branch", "total_fine"]
    list_filter = ("first_name", "last_name", "user_id", "total_fine", )

class BookDetailModelAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "books_count", "category"]
    list_filter = ("title", "author", "category", )

    class Meta:
        model = BookDetail


class BookModelAdmin(admin.ModelAdmin):
    list_display = ["get_title", "avail_status", "shelf_no"]
    list_filter = ("book_id", "avail_status", )
    # get_title is a method in Book class to retrieve Book's title using foreign key relationship


    list_per_page = 3
    
    class Meta:
        model = Book


admin.site.register(BookDetail, BookDetailModelAdmin)
admin.site.register(Book, BookModelAdmin)
admin.site.register(Student, StudentModelAdmin)
admin.site.register(IssueDetail, IssueDetailModelAdmin)
