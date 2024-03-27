from django import forms


class ProdutoForm(forms.Form):
    nome = forms.CharField(label="Nome", max_length=255)
    descricao = forms.CharField(label="Descrição", max_length=255)
    preco = forms.FloatField(label="Preço")
    quantidade = forms.IntegerField(label="Quantidade")