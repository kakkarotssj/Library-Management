# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Student(models.Model):
    first_name         = models.CharField(max_length=120)
    last_name          = models.CharField(max_length=120)
    email_id           = models.EmailField(unique=True)
    password           = models.CharField(max_length=120)
    contact_no         = models.BigIntegerField(unique=True)
    user_id            = models.CharField(max_length=120, unique=True)
    books_issued_count = models.PositiveSmallIntegerField(default=0)
    total_fine         = models.PositiveSmallIntegerField(default=0)
    branch             = models.CharField(max_length=120)

    def __unicode__(self):
        return '{} {} {} {} {}'.format(self.first_name, self.last_name, self.user_id, self.branch, self.books_issued_count)

    def __str__(self):
        return '{} {} {} {} {}'.format(self.first_name, self.last_name, self.user_id, self.branch, self.books_issued_count)

    '''

                                ***** STUDENTS *****
    S.No.   FirstName   LastName    EmailId                 Password    ContactNo       UserId      BooksIssueCount     TotalFine   Branch       

    1       Siddharth   Sharma      15UCS141@lnmiit.ac.in   sharma      1231231231      15UCS141    0                   0           CSE
    2       Smriti      Jha         15UCS142@lnmiit.ac.in   Jha         3213213213      15UCS142    0                   0           CSE
    3       Vikram      Raj         15UME030@lnmiit.ac.in   raj         4564564564      15UME030    0                   0           ME
    '''


class BookDetail(models.Model):
    title       = models.CharField(max_length=120, unique=True)
    author      = models.CharField(max_length=120)
    publisher   = models.CharField(max_length=120)
    books_count = models.PositiveSmallIntegerField()
    category    = models.CharField(max_length=120)

    def __unicode__(self):
        return '{} {} {} {}'.format(self.title, self.author, self.books_count, self.category)

    def __str__(self):
        return '{} {} {} {}'.format(self.title, self.author, self.books_count, self.category)

    '''
                                ***** BOOKDETAIL *****

        S.No.       Title                       Author                  Publisher           Books Count         Category

        1           Encyclopedia                Sidhu paaji             satakli             5                   ALL
        2           Heat Transfer               Goku                    whoops              2                   ME
        3           Intro to Algorithms         abba jabba              jabba abba          3                   CSE    

    '''


class Book(models.Model):
    book_id      = models.ForeignKey(BookDetail, on_delete=models.CASCADE)
    isbn_no      = models.PositiveIntegerField(unique=True)
    avail_status = models.CharField(max_length=120)
    shelf_no     = models.CharField(max_length=120, unique=True)
    total_issues = models.PositiveSmallIntegerField()

    def __unicode__(self):
        return '{} {} {}'.format(self.book_id.title, self.avail_status, self.shelf_no)

    def __str__(self):
        return '{} {} {}'.format(self.book_id.title, self.avail_status, self.shelf_no)

    def get_title(self):
        return self.book_id.title

    '''
                                    ***** BOOK *****

    S.No.        Book Id                    Isbn no:        Avail Status        Shelf no.       Total Issues

    1            Intro to Algorithms        450             yes                 165             5
    2            Intro to Algorithms        20220           yes                 154             546
    3            Intro to Algorithms        2500            yes                 123             500
    4            Heat Transfer              4561            yes                 456465          212
    5            Heat Transfer              2141            yes                 111             212
    6            Encyclopedia               123123          yes                 7878            65
    7            Encyclopedia               645             yes                 784             547
    8            Encyclopedia               44              yes                 000             12
    9            Encyclopedia               911             yes                 911             41
    10           Encyclopedia               100             yes                 100             30

    '''


class IssueDetail(models.Model):
    book_id     = models.ForeignKey(Book, on_delete=models.CASCADE)
    student_id  = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.book_id.book_id.title, self.student_id.user_id)

    def __unicode__(self):
        return '{} {}'.format(self.book_id.book_id.title, self.student_id.user_id)

    def get_book_title(self):
        return self.book_id.book_id.title

    def get_student_id(self):
        return self.student_id.user_id

    '''

                                ***** ISSUE DETAILS *****

        S.No.   Book Id                 Student Id
        1       Encyclopedia            15UCS141
        2       Encyclopedia            15UME030
        3       Intro to Algorithms     15UME030
        4       Heat Transfer           15UCS142

    '''