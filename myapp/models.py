from django.db import models

# Create your models here.


class Cliente(models.Model):


    nome = models.CharField(max_length=45)
    data_pagamento = models.DateField()
    descricao = models.TextField()
    entrega = models.BooleanField(default=False)
    saldo = models.DecimalField(max_digits=6, decimal_places=2)

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
