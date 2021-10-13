from django.db import models

# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(max_length=600)
    preco = models.DecimalField(max_digits=9, decimal_places=2)
    tipo_unidade = models.CharField(max_length=200, default="unidades")
    valor_unidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.nome} - {self.valor_unidade} {self.tipo_unidade} - R$ {self.preco}"
