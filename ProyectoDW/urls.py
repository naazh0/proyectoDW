"""ProyectoDW URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from noticias import views
from django.contrib.auth.views import login, logout


urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('noticias.urls',namespace='noticias')),
	url(r'^signup$', views.signup, name='signup'),
    url(r'^login$', login, {'template_name':'login.html'}, name="login"),
    url(r'^home$', views.home, name='home'),
    url(r'^logout$', logout, {'template_name': 'noticias/main.html', }, name="logout"),
    url(r'^perfil$', views.perfil, name='perfil'),
    url(r'^$', views.main, name='main'),
    url(r'^detalle/(?P<pk>\d+)$', views.detalle_noticia, name='detalle'),
    url(r'^new/$', views.editar_copro, name='editar_copro'),
    url(r'^edit/(?P<pk>\d+)$', views.copro_update, name='copro_update'),
    url(r'^delete/(?P<pk>\d+)$', views.copro_delete, name='copro_delete'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

