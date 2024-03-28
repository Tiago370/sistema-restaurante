from django.contrib import admin

# Register your models here.
from .models import Produto, Cliente, Entregador, Pedido

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'descricao', 'quantidade')

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'whatsapp')

class EntregadorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'cpf')

class PedidoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'entregador', 'status')

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Entregador, EntregadorAdmin)
admin.site.register(Pedido, PedidoAdmin)