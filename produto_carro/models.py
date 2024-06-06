from django.db import models
from produtos.models import Produto
# Create your models here.
class Carro(Produto):
    cor = models.CharField(max_length=255)
