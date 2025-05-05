from django.db import models


class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

#=============================================

class Produto(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    codigo = models.CharField(max_length=8, unique=True)
    categoria_id = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='produtos')
    quantidade = models.PositiveIntegerField()
    preco_compra = models.DecimalField(max_digits=10, decimal_places=2)
    preco_venda = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.CharField(max_length=400)
    estoque_minimo = models.IntegerField(default=0)
    
    def __str__(self):
        return self.nome

#=============================================

class Pedido(models.Model):
    id = models.AutoField(primary_key=True)
    nome_cliente = models.CharField(max_length=200)
    data_pedido = models.DateField(auto_now=True)
    forma_pagamento = models.CharField(max_length=100)
    valor_compra = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.nome_cliente

    def calcular_valor_total(self):
        total = sum(item.subtotal() for item in self.itens.all())  
        self.valor_compra = total  
        self.save()  

#=============================================

class itemPedido(models.Model):
    id = models.AutoField(primary_key=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='item_pedidos')
    quantidade = models.PositiveIntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantidade} x {self.produto.nome}"

    def subtotal(self):
        return self.quantidade * self.preco_unitario  

#=============================================

class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    telefone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.nome

#=============================================

created_at = models.DateTimeField(auto_now_add=True)
updated_at =  models.DateTimeField(auto_now=True)