from django.conf.urls import url
from RestApp import views

urlpatterns = [
    url(r'^factors/$', views.factor_list),
]
