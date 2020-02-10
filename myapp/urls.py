from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('clientes', views.ClienteView)
router.register('usuarios', views.UsuarioView)
router.register('estabelecimento', views.EstabelecimentoView)
router.register('entrega', views.EntregaView)
router.register('cardapio', views.CardapioView)
router.register('rota', views.RotaView)
router.register('telefones', views.TelefoneView)
router.register('pedido', views.PedidoView)
router.register('conta_receber', views.Conta_receberView)
router.register('dias_pedido', views.Dias_pedidoView)
router.register('produto', views.ProdutoView)
router.register('item', views.ItemView)
router.register('preco_produto', views.Preco_produtoView)
router.register('perfil', views.PerfilView)
router.register('menu', views.MenuView)
router.register('funcionalidade', views.FuncionalidadeView)


urlpatterns = [

    #url('', views.ClienteList.as_view(), name='cliente-list'),
    path('', include(router.urls))

]