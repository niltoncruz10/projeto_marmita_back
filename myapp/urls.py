from django.conf.urls import url
from . import views

urlpatterns = [
    url('', views.ClienteList.as_view(), name='cliente-list'),

]