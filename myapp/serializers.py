from rest_framework import serializers
from .models import Cliente, Estabelecimento, Entrega, Cardapio

class ClienteSerializer(serializers.ModelSerializer):

    class Meta:

        model = Cliente
        fields = ('id', 'nome', 'data_pagamento', 'descricao', 'entrega', 'saldo')


class EstabelecimentoSerializer(serializers.ModelSerializer):

    class Meta:

        model = Estabelecimento
        fields = ('id', 'nome', 'razao_social', 'cpf_cnpj', 'email', 'telefone', 'responsavel')


class EntregaSerializer(serializers.ModelSerializer):

    class Meta:

        model = Entrega
        fields = ('id', 'taxa_entrega')


class CardapioSerializer(serializers.ModelSerializer):

    class Meta:

        model = Cardapio
        fields = ('id', 'item_cardapio')


class RotaSerializer(serializers.ModelSerializer):

    class Meta:

        model = Rota
        fields = ('id', 'identificador', 'descricao', )