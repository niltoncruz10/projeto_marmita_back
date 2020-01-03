from django.contrib import admin
from .models import Cliente, Cardapio, Entrega, Estabelecimento, Rota, Telefone, Pedido, Conta_receber, Dias_pedido, \
    Produto, Item, Preco_produto

# Register your models here.



admin.site.register(Cliente)
admin.site.register(Cardapio)
admin.site.register(Entrega)
admin.site.register(Estabelecimento)
admin.site.register(Rota)
admin.site.register(Telefone)
admin.site.register(Pedido)
admin.site.register(Conta_receber)
admin.site.register(Dias_pedido)
admin.site.register(Produto)
admin.site.register(Item)
admin.site.register(Preco_produto)