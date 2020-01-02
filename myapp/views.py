#from rest_framework import generics
from .models import Cliente, Estabelecimento, Entrega, Cardapio, Rota, Telefone, Pedido
from .serializers import ClienteSerializer, EstabelecimentoSerializer, EntregaSerializer, CardapioSerializer,\
    RotaSerializer, TelefoneSerializer, PedidoSerializer
from rest_framework import viewsets

#class ClienteList(generics.ListCreateAPIView):


class ClienteView(viewsets.ModelViewSet):

    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


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


