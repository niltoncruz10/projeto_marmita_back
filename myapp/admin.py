from django.contrib import admin
from .models import Cliente, Usuario, Cardapio, Entrega, Estabelecimento, Rota, Telefone, Pedido, Conta_receber, Dias_pedido, \
    Produto, Item, Preco_produto, Perfil, Menu, Funcionalidade

# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_pagamento', 'entrega', 'saldo', 'descricao')
    list_filter = ('nome', 'data_pagamento',)

class EstabelecimentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'razao_social', 'cpf_cnpj', 'email', 'telefone', 'responsavel')


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'status')


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Cardapio)
admin.site.register(Entrega)
admin.site.register(Estabelecimento, EstabelecimentoAdmin)
admin.site.register(Rota)
admin.site.register(Telefone)
admin.site.register(Pedido)
admin.site.register(Conta_receber)
admin.site.register(Dias_pedido)
admin.site.register(Produto)
admin.site.register(Item)
admin.site.register(Preco_produto)
admin.site.register(Perfil)
admin.site.register(Menu)
admin.site.register(Funcionalidade)

