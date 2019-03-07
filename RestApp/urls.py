from django.conf.urls import url
from RestApp import views

urlpatterns = [
    url(r'^factors/$', views.factor_list),
    url(r'^factors/(?P<pk>[0-9]+)/$', views.factor_detail),
]
