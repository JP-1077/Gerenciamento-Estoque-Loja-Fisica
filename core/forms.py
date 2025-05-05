from django import forms
from .models import Produto, Pedido, itemPedido


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'codigo', 'categoria_id', 'quantidade', 'preco_compra', 'preco_venda', 'descricao', 'estoque_minimo']

# Formulário de Pedido
class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['nome_cliente', 'forma_pagamento']

# Formulário de Item do Pedido
class ItemPedidoForm(forms.ModelForm):
    class Meta:
        model = itemPedido
        fields = ['produto', 'quantidade', 'preco_unitario']

