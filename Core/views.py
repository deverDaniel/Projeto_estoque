from django.shortcuts import render, redirect, get_object_or_404
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
    valor = 0
    for produto in produtos:
        prod_ingredientes = ProdutoIngrediente.objects.filter(produto=produto)
        for prod_ingrediente in prod_ingredientes:
            valor += ( prod_ingrediente.quantidade / 1000 ) * prod_ingrediente.ingrediente.preco
        produto.preco_custo = valor
        valor = 0
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

def Atualiza_ingrediente(request,id):
    ingrediente = get_object_or_404(Ingrediente,id=id)
    data = {}
    form = IngredienteForm(request.POST or None, instance= ingrediente)
    data['ingrediente'] = ingrediente
    data['form'] = form
    if request.method == 'POST':
        if form .is_valid():
            form.save()
            return redirect('core_ingredientes')
    else:
        return render(request, 'core/update_ingrediente.html', data)

def Deletar_ingrediente(request,id):
    ingrediente = get_object_or_404(Ingrediente,id=id)
    if request.method == 'POST':
        ingrediente.delete()
        return redirect('core_ingredientes')
    else:
        return render(request, 'core/delete_confirm.html', {"obj": ingrediente})

def Atualiza_Produto_Ingrediente(request, produto_id, ingrediente_id):
    produtoIngrediente = get_object_or_404(ProdutoIngrediente,produto = produto_id, ingrediente = ingrediente_id)
    data = {}
    form = ProdutoIngredienteForm(request.POST or None, instance= produtoIngrediente)
    data['produto'] = produtoIngrediente.produto
    data['ingrediente'] = produtoIngrediente.ingrediente
    data['form'] = form
    if request.method == 'POST':
        if form .is_valid():
            form.save()
            return redirect('core_adicionar_ingrediente', produto_id)
    else:
        return render(request, 'core/update_produto_ingrediente.html', data)

def Deletar_Produto_Ingrediente(request,produto_id, ingrediente_id):
    produtoIngrediente = get_object_or_404(ProdutoIngrediente,produto = produto_id, ingrediente = ingrediente_id)
    if request.method == 'POST':
        produtoIngrediente.delete()
        return redirect('core_adicionar_ingrediente', produto_id)
    else:
        return render(request, 'core/delete_confirm.html', {"obj": produtoIngrediente.ingrediente})
