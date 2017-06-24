from django.conf.urls import url
from noticias import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^$', views.main, name='main'),
    
    
    
    
]
