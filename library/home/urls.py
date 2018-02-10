from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^signup$', views.signup, name='signup'),
    url(r'^login$', views.login, name='login'),
    url(r'^student_profile$', views.student_profile, name='student_profile'),
    url(r'^logout$', views.logout, name='logout'),
]
