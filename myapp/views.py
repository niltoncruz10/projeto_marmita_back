#from rest_framework import generics
from .models import Cliente, Estabelecimento
from .serializers import ClienteSerializer, EstabelecimentoSerializer
from rest_framework import viewsets

#class ClienteList(generics.ListCreateAPIView):
class ClienteView(viewsets.ModelViewSet):

    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class EstabelecimentoView(viewsets.ModelViewSet):

        queryset = Estabelecimento.objects.all()
        serializer_class = EstabelecimentoSerializer