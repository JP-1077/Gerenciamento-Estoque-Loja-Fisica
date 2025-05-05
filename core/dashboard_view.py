from django.db.models import Sum, F
from django.shortcuts import render
from .models import Produto, Pedido

def dashboard_view(request):
    produtos_alerta = Produto.objects.filter(quantidade__lt=F('estoque_minimo'))

    produtos_mais_vendidos = Produto.objects.annotate(
        total_vendido=Sum('item_pedidos__quantidade')
    ).order_by('-total_vendido')[:5]

    principais_clientes = Pedido.objects.values('nome_cliente').annotate(
        total_gasto=Sum('valor_compra')
    ).order_by('-total_gasto')[:5]

    produtos_em_estoque = Produto.objects.filter(quantidade__gt=0)

    context = {
        'produtos_alerta': produtos_alerta,
        'produtos_mais_vendidos': produtos_mais_vendidos,
        'principais_clientes': principais_clientes,
        'produtos_em_estoque': produtos_em_estoque,
    }

    return render(request, 'dashboard.html', context)

