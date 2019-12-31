from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('clientes', views.ClienteView)
router.register('estabelecimento', views.EstabelecimentoView)

urlpatterns = [

    #url('', views.ClienteList.as_view(), name='cliente-list'),
    path('', include(router.urls))

]