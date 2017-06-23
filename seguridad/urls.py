from django.conf.urls import url
from seguridad.views import Login

urlpatterns = [
        url(r'^$', Login.as_view(), name="login"),
]