from django.db import models

# Create your models here.


class Cliente(models.Model):

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