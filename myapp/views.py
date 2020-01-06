#from rest_framework import generics
from .models import Cliente, Usuario, Estabelecimento, Entrega, Cardapio, Rota, Telefone, Pedido, Conta_receber, \
    Dias_pedido, Produto, Item, Preco_produto, Perfil, Menu, Funcionalidade
from .serializers import ClienteSerializer, UsuarioSerializer, EstabelecimentoSerializer, EntregaSerializer, \
    CardapioSerializer, RotaSerializer, TelefoneSerializer, PedidoSerializer, Conta_receberSerializer, \
    Dias_pedidoSerializer, ProdutoSerializer, ItemSerializer, Preco_produtoSerializer, PerfilSerializer, \
    MenuSerializer, FuncionalidadeSerializer
from rest_framework import viewsets

#class ClienteList(generics.ListCreateAPIView):


class ClienteView(viewsets.ModelViewSet):

    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class UsuarioView(viewsets.ModelViewSet):

    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class EstabelecimentoView(viewsets.ModelViewSet):

    queryset = Estabelecimento.objects.all()
    serializer_class = EstabelecimentoSerializer


class EntregaView(viewsets.ModelViewSet):

    queryset = Entrega.objects.all()
    serializer_class = EntregaSerializer


class CardapioView(viewsets.ModelViewSet):

    queryset = Cardapio.objects.all()
    serializer_class = CardapioSerializer


class RotaView(viewsets.ModelViewSet):

    queryset = Rota.objects.all()
    serializer_class = RotaSerializer


class TelefoneView(viewsets.ModelViewSet):

    queryset = Telefone.objects.all()
    serializer_class = TelefoneSerializer


class PedidoView(viewsets.ModelViewSet):

    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer


class Conta_receberView(viewsets.ModelViewSet):

    queryset = Conta_receber.objects.all()
    serializer_class = Conta_receberSerializer


class Dias_pedidoView(viewsets.ModelViewSet):

    queryset = Dias_pedido.objects.all()
    serializer_class = Dias_pedidoSerializer


class ProdutoView(viewsets.ModelViewSet):

    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


class ItemView(viewsets.ModelViewSet):

    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class Preco_produtoView(viewsets.ModelViewSet):

    queryset = Preco_produto.objects.all()
    serializer_class = Preco_produtoSerializer


class PerfilView(viewsets.ModelViewSet):

    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer


class MenuView(viewsets.ModelViewSet):

    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class FuncionalidadeView(viewsets.ModelViewSet):
    queryset = Funcionalidade.objects.all()
    serializer_class = FuncionalidadeSerializer
