from django.db import models

# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(max_length=600)
    preco = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return f"{self.nome} - R$ {self.preco}"
