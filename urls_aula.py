from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^(P<carro_id>[0-9]+)/$', views.detail),
]
