from django.db import models

# Create your models here.
class Produtos(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255, null=True)
    preco = models.FloatField()
    quantidade = models.IntegerField()