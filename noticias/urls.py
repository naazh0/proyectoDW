from django.conf.urls import url
from noticias import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]