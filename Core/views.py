from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Ingrediente, Produto, ProdutoIngrediente
from .form import IngredienteForm, ProdutoForm, ProdutoIngredienteForm, SearchForm

def home(request):
    query = request.GET.get('query', '')
    produtos = Produto.objects.all()

    if query:
        produtos = produtos.filter(nome__icontains =query)  # Altere 'nome' para o campo que você deseja pesquisar

    paginator = Paginator(produtos, 3)  # 3 é o número máximo de itens por página
    page_number = request.GET.get('page')  # Pega o número da página da URL
    produtos = paginator.get_page(page_number)

    form = SearchForm(request.GET)
    data = {'produtos': produtos, 'form': form}
    return render(request, 'core/index.html', data)

def ingredientes(request):
    ingredientes =  Ingrediente.objects.all()
    form = IngredienteForm()
    data = {'ingredientes': ingredientes, "form": form}
    return render(request, 'core/lista_ingredientes.html', data)

def produtos(request):
    produtos = Produto.objects.all()
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

def adicionar_pruduto_pronto(request, id):
    return redirect('core_produtos')

def pesquisar(request):
    query = request.GET.get('query', '')
    produtos = Produto.objects.all()

    if query:
        produtos = produtos.filter(nome=query)  # Altere 'nome' para o campo que você deseja pesquisar

    form = SearchForm(request.GET)
    return render(request, 'tabela.html', {'form': form, 'produtos': produtos})
