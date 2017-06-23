from django.conf.urls import url
from noticias import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>\d+)$', views.detalle_noticia, name='detalle_noticia'),
]