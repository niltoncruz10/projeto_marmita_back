from rest_framework import serializers
from .models import Cliente, Usuario, Estabelecimento, Entrega, Cardapio, Rota, Telefone, Pedido, Conta_receber, Dias_pedido, \
    Produto, Item, Preco_produto, Perfil, Menu, Funcionalidade

class ClienteSerializer(serializers.ModelSerializer):

    class Meta:

        model = Cliente
        fields = ('id', 'nome', 'data_pagamento', 'descricao', 'entrega', 'saldo')


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'nome', 'status')


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
        fields = ('id', 'identificador', 'descricao')


class TelefoneSerializer(serializers.ModelSerializer):

    class Meta:

        model = Telefone
        fields = ('id', 'ddd', 'numero', 'cliente')


class PedidoSerializer(serializers.ModelSerializer):

    class Meta:

        model = Pedido
        fields = ('id', 'status', 'valor')


class Conta_receberSerializer(serializers.ModelSerializer):

    class Meta:

        model = Conta_receber
        fields = ('id', 'valor', 'valor_pago', 'status')


class Dias_pedidoSerializer(serializers.ModelSerializer):

    class Meta:

        model = Dias_pedido
        fields = ('id', 'segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo')


class ProdutoSerializer(serializers.ModelSerializer):

    class Meta:

        model = Produto
        fields = ('id', 'nome', 'descricao')


class ItemSerializer(serializers.ModelSerializer):

    class Meta:

        model = Item
        fields = ('id', 'nome')


class Preco_produtoSerializer(serializers.ModelSerializer):

    class Meta:

        model = Preco_produto
        fields = ('id', 'valor')


class PerfilSerializer(serializers.ModelSerializer):

    class Meta:

        model = Perfil
        fields = ('id', 'nome', 'descricao')


class MenuSerializer(serializers.ModelSerializer):

    class Meta:

        model = Menu
        fields = ('id', 'titulo', 'icone')


class FuncionalidadeSerializer(serializers.ModelSerializer):

    class Meta:

        model = Funcionalidade
        fields = ('id', 'titulo', 'link')