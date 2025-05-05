from django.urls import path
from .produtos_views import produto_lista, produto_detalhe, produto_criar, produto_update
from .pedido_views import lista_pedidos, detalhe_pedidos,  criar_pedido
from .dashboard_view import dashboard_view
from .home_views import home_view
from .capa_views import capa

urlpatterns = [

    # Rota da Página HOME
    path('', capa, name='capa'),
    path('home/', home_view, name='home'),

    # Rotas de Produtos
    path('produtos/', produto_lista, name='produto_lista'),
    path('produtos/<int:pk>/', produto_detalhe, name='produto_detalhe'),
    path('produtos/novo/', produto_criar, name='produto_criar'),
    path('produtos/<int:pk>/editar/', produto_update, name='produto_update'),

    # Rotas de Pedido
    path('pedidos/', lista_pedidos, name = 'lista_pedidos'),
    path('pedidos/<int:pk>/', detalhe_pedidos, name = 'pedido_detalhe'),
    path('pedidos/novo/', criar_pedido, name='criar_pedido'),

    # Rota do Dashboard
    path('dashboard/', dashboard_view, name = 'dashboard')
]
