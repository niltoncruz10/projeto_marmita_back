from django.db import models

# Create your models here.


class Cliente(models.Model):

    class Meta:

        db_table = 'cliente'

    nome = models.CharField(max_length=45)
    data_pagamento = models.DateField()
    descricao = models.TextField()
    entrega = models.BooleanField(default=False)
    saldo = models.DecimalField(max_digits=6, decimal_places=2)

    def__str__(self):
    return self.nome


