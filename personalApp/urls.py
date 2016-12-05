from django.conf.urls import url
from . import views

app_name = 'personalApp'

urlpatterns = [
    url(r'^$', views.index, name="home"),
    url(r'^contact/$', views.contact, name="contact"),
    url(r'^news/$', views.news, name="news"),
]
