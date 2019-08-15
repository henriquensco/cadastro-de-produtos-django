from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Produtos
from .forms import ProdutosForm


#Metodo responsavel por VISUALIZAR os Produtos
@login_required
def HomePage(request):
    buscar_produtos = Produtos.objects.all()
    return render(request, 'home_page.html', {'produtos': buscar_produtos})


#Metodo responsavel por fazer o CREATE do Produto
@login_required
def CadastarProduto(request):
    form = ProdutosForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('homepage')
    return render(request, 'novo_produto.html', {'form': form})

#Metodo responsavel por fazer um UPDATE do Produto
@login_required
def EditarProduto(request, pk):
    buscar_produtos = get_object_or_404(Produtos, pk=pk)
    form = ProdutosForm(request.POST or None, request.FILES or None, instance=buscar_produtos)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('homepage')
    return render(request, 'editar_produto.html', {'form': form})

#Metodo responsavel por fazer o VISUALIZAR os detalhes do Produto
@login_required
def DetalhesProduto(request, pk):
    buscar_produtos = get_object_or_404(Produtos, pk=pk)
    return render(request, 'detalhes_produto.html', {'detalhes': buscar_produtos})

#Metodo responsavel por fazer o DELETE do Produto
@login_required
def DeletarProduto(request, pk):
    buscar_produtos = get_object_or_404(Produtos, pk=pk)
    #form = ProdutosForm(request.POST or None, request.FILES or None, instance=buscar_produtos)
    if request.method == 'POST':
        buscar_produtos.delete()
        return redirect('homepage')

    return render(request, 'deletar_produto.html', {'deletar': buscar_produtos})
