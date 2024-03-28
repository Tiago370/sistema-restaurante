from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .forms import ProdutoForm
from produtos.models import Produto

def produtos(request):
    if request.method == "POST":
        form = ProdutoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data["nome"]
            decricao = form.cleaned_data["descricao"]
            preco = form.cleaned_data["preco"]
            quantidade = form.cleaned_data["quantidade"]

            produto = Produtos(nome=nome, descricao=decricao, preco=preco, quantidade=quantidade)
            produto.save()
            form = ProdutoForm()   
            return render(request, 'produtos.html', {"produtos": Produtos.objects.all().values(), 'form':form})
    else:
        form = ProdutoForm()

        return render(request, 'produtos.html', {"form": form})
