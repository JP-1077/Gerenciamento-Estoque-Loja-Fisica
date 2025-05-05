from django.shortcuts import render, redirect, get_object_or_404
from .models import Pedido, itemPedido, Produto
from .forms import ProdutoForm, PedidoForm, ItemPedidoForm
from django.forms import inlineformset_factory


# Listagem dos Produtos

def lista_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request,'pedidos_lista.html', {'pedidos':pedidos})

#=====================================================================

# Visualizar detalhes dos Pedidos

def detalhe_pedidos(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    return render(request, 'pedido_detalhe.html', {'pedido':pedido})

#=====================================================================

# Criar novo pedido

def criar_pedido(request):
    ItemPedidoFormSet = inlineformset_factory(Pedido, itemPedido, form=ItemPedidoForm, extra=1, can_delete=True)

    if request.method == 'POST':
        pedido_form = PedidoForm(request.POST)
        formset = ItemPedidoFormSet(request.POST)

        if pedido_form.is_valid() and formset.is_valid():
            pedido = pedido_form.save()
            formset.instance = pedido
            formset.save()

            pedido.calcular_valor_total()

            for item in pedido.itens.all():
                produto = item.produto
                produto.quantidade -= item.quantidade
                produto.save()

            return redirect('pedido_detalhe', pk=pedido.pk)
        
    else:
        pedido_form = PedidoForm()
        formset = ItemPedidoFormSet()

    return render(request, 'pedidos/pedido_form.html', {
        'pedido_form': pedido_form,
        'formset': formset,

    })

#=====================================================================

