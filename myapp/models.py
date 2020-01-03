from django.db import models

# Create your models here.


class Cliente(models.Model):

    estabelecimento = models.ForeignKey("Estabelecimento", on_delete=models.CASCADE, related_name='cliente')
    nome = models.CharField(max_length=45)
    data_pagamento = models.DateField()
    descricao = models.CharField(max_length=45, blank=True)
    entrega = models.BooleanField(default=False)
    saldo = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.nome


class Estabelecimento(models.Model):


    nome = models.CharField(max_length=45)
    razao_social = models.CharField(max_length=45)
    cpf_cnpj = models.CharField(max_length=18)
    email = models.CharField(max_length=45)
    telefone = models.CharField(max_length=45)
    responsavel = models.CharField(max_length=45)

    def __str__(self):
        return self.nome


class Entrega(models.Model):

    taxa_entrega = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.taxa_entrega


class Cardapio(models.Model):

    item_cardapio = models.CharField(max_length=45)

    def __str__(self):
        return self.item_cardapio


class Rota(models.Model):

    identificador = models.CharField(max_length=8)
    descricao = models.CharField(max_length=45)

    def __str__(self):
        return self.identificador


class Telefone(models.Model):

    ddd = models.CharField(max_length=3)
    numero = models.CharField(max_length=10)
    cliente = models.OneToOneField(Cliente, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.numero


class Pedido(models.Model):

    status = models.BooleanField(default=False)
    valor_total = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.status


class Conta_receber(models.Model):

    valor = models.DecimalField(max_digits=6, decimal_places=2)
    valor_pago = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.valor_pago


class Dias_pedido(models.Model):

    segunda = models.BooleanField(default=False)
    terca = models.BooleanField(default=False)
    quarta = models.BooleanField(default=False)
    quinta = models.BooleanField(default=False)
    sexta = models.BooleanField(default=False)
    sabado = models.BooleanField(default=False)
    domingo = models.BooleanField(default=False)

    def __str__(self):
        return self.segunda


class Produto(models.Model):

    nome = models.CharField(max_length=30)
    descricao = models.CharField(max_length=40)
    #preco_produto = models.OneToOneField(Preco_produto, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome


class Item(models.Model):

    nome = models.CharField(max_length=30)
    descricao = models.CharField(max_length=40)
    entrega = models.BooleanField(default=False)

    def __str__(self):
        return self.nome


class Preco_produto(models.Model):

    valor = models.DecimalField(max_digits=6, decimal_places=2)
    #produto = models.OneToOneField(Produto, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return self.valor