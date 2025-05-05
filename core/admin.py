from django.contrib import admin
from .models import Categoria, Produto, Cliente, Pedido, itemPedido

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('nome',)

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ( 'id', 'nome', 'codigo', 'categoria_id', 'quantidade', 'preco_compra', 'preco_venda', 'descricao', 'estoque_minimo')
    list_filter = ('categoria_id',)
    search_fields = ('nome',)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'telefone')
    search_fields = ('nome', 'email')

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_cliente', 'data_pedido', 'forma_pagamento', 'valor_compra')
    list_filter = ('forma_pagamento', 'data_pedido')
    search_fields =('nome_cliente',)

@admin.register(itemPedido)
class ItemPedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'pedido', 'produto', 'quantidade', 'get_subtotal')
    list_filter =  ('produto',)

    def get_subtotal(self, obj):
        return obj.subtotal()
    
    get_subtotal.short_description = "Subtotal"



