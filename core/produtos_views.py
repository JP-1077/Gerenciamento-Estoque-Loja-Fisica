from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto
from .forms import ProdutoForm



# Listagem dos Produtos

def produto_lista(request):
    ordenacao = request.GET.get('ordenar', 'nome')
    produtos = Produto.objects.all().order_by(ordenacao)
    return render(request, 'produto_list.html', {'produtos': produtos})

#=====================================================================

# Capturar detalhe do produto

def produto_detalhe(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    return render(request, 'produto_detail.html', {'produto': produto})

#=====================================================================

# Cadastrar novo Produto

def produto_criar(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produto_lista')
    else:
        form = ProdutoForm()
    return render(request, 'produto_form.html', {'form': form})

#=====================================================================

# Editar produto

def produto_update(request, pk):
    produto = get_object_or_404(Produto,pk=pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('produto_lista')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'produto_form.html', {'form': form})

#=====================================================================


