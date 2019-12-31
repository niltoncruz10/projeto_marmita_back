from rest_framework import generics
from .models import Cliente
from .serializers import ClienteSerializer

# Create your views here.
class ClienteList(generics.ListCreateAPIView):

    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer