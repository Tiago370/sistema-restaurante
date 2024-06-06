from django.contrib import admin
from produtos.admin import ProdutoAdmin
from .models import Produto
from .models import Carro

# Register your models here.
class CarroAdmin(ProdutoAdmin):
    list_display = ('cor','nome', 'preco', 'descricao', 'quantidade')

admin.site.unregister(Produto)
admin.site.register(Carro, CarroAdmin)
