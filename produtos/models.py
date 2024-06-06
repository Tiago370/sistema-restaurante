from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255, null=True)
    preco = models.FloatField()
    quantidade = models.IntegerField()

    def __str__(self):
        return self.nome
    
class Cliente(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255, null=True)
    whatsapp = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.nome

class Entregador(models.Model):
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=255, null=True)
    cpf = models.CharField(max_length=255, null=True)
    placa = models.CharField(max_length=255, null=True)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = "Entregadores"

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    entregador = models.ForeignKey(Entregador, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=255, default="Pendente")
    produtos = models.ManyToManyField(Produto)