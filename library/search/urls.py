from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.search_books, name='search_book'),
    url(r'^(?P<book_id>\d+)$', views.list_books, name='list_books'),
]