from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from noticias import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^$', views.main, name='main'),
	   
    
    
    
]
