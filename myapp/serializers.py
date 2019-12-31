from rest_framework import serializers
from .models import Cliente
from .models import Estabelecimento

class ClienteSerializer(serializers.ModelSerializer):

    class Meta:

        model = Cliente
        fields = ('id', 'nome', 'data_pagamento', 'descricao', 'entrega', 'saldo')


class EstabelecimentoSerializer(serializers.ModelSerializer):

    class Meta:

        model = Estabelecimento
        fields = ('id', 'nome', 'razao_social', 'cpf_cnpj', 'email', 'telefone', 'responsavel')
