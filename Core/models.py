from django.db import models

# Modelo Ingrediente
class Ingrediente(models.Model):
    nome = models.CharField(max_length=100)
    estoque_min = models.FloatField()
    estoque_atual = models.FloatField()
    unidade_medida = models.CharField(max_length = 20, default="Gramas")
    preco = models.FloatField(default= 0)

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
    class Meta:
        # Usando UniqueConstraint para garantir a unicidade da combinação de produto e ingrediente
        constraints = [
            models.UniqueConstraint(fields=['produto', 'ingrediente'], name='unique_produto_ingrediente')
        ]
        unique_together = ('produto', 'ingrediente')  # ou constraints com UniqueConstraint para versões anteriores

    id = models.AutoField(primary_key=True)
    def __str__(self):
        return f"{self.quantidade} de {self.ingrediente.nome} em {self.produto.nome}"
