from django.db import models

# Modelo Ingrediente
class Ingrediente(models.Model):
    nome = models.CharField(max_length=100)
    estoque_min = models.FloatField()
    estoque_atual = models.FloatField()
    unidade_medida = models.CharField(max_length = 20, default="0")
    descricao = models.CharField(max_length=200, default= "0")

    def __str__(self):
        return self.nome

# Modelo Produto
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco_unitario = models.FloatField()
    quantidade_estoque = models.FloatField()
    min_estoque = models.FloatField(default=0)
    def __str__(self):
        return self.nome

# Tabela intermediária para associar os ingredientes com o produto e registrar a quantidade
class ProdutoIngrediente(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)  # Relacionamento com Produto
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)  # Relacionamento com Ingrediente
    quantidade = models.FloatField()  # Quantidade de ingrediente necessária para o produto
    def __str__(self):
        return f"{self.quantidade} de {self.ingrediente.nome} em {self.produto.nome}"
