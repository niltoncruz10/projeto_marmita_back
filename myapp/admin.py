from django.contrib import admin
from .models import Cliente, Cardapio, Entrega, Estabelecimento, Rota, Telefone, Pedido

# Register your models here.



admin.site.register(Cliente)
admin.site.register(Cardapio)
admin.site.register(Entrega)
admin.site.register(Estabelecimento)
admin.site.register(Rota)
admin.site.register(Telefone)
admin.site.register(Pedido)