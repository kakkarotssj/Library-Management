from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.search_books, name='search_book'),
]