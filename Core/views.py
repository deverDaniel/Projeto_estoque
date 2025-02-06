from django.shortcuts import render, redirect
from .models import Ingrediente, Produto, ProdutoIngrediente
from .form import IngredienteForm, ProdutoForm, ProdutoIngredienteForm

def home(request):
    return render(request, 'core/index.html')

def ingredientes(request):
    ingredientes =  Ingrediente.objects.all()
    form = IngredienteForm()
    data = {'ingredientes': ingredientes, "form": form}
    return render(request, 'core/lista_ingredientes.html', data)

def produtos(request):
    produtos =  Produto.objects.all()
    form = ProdutoForm()
    data = {'produtos': produtos, "form": form}
    return render(request, 'core/lista_produtos.html', data)

def Ingrediente_novo(request):
    form = IngredienteForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_ingredientes')

def Produto_novo(request):
    form = ProdutoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_produtos')


def adicionar_ingrediente(request, id):
    produto = Produto.objects.get(id=id)
    receitas = ProdutoIngrediente.objects.filter(produto = produto)
    if request.method == 'POST':
        form = ProdutoIngredienteForm(request.POST)
        if form.is_valid():
            form_ingrediente = form.save(commit=False)
            form_ingrediente.produto = produto
            form_ingrediente.save()
            return redirect('core_adicionar_ingrediente', produto.id)  # Redireciona para a página de sucesso ou uma página específica
    else:
        form = ProdutoIngredienteForm()
    data = {'form': form, 'receitas': receitas, 'produto': produto}
    return render(request, 'core/adicionar_ingrediente.html', data)
