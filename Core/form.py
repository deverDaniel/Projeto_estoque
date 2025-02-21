from django.forms import ModelForm
from django import forms
from .models import Ingrediente, Produto, ProdutoIngrediente

class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'

class IngredienteForm(ModelForm):
    class Meta:
        model = Ingrediente
        fields = '__all__'

class ProdutoIngredienteForm(ModelForm):
    class Meta:
        model = ProdutoIngrediente
        fields = ['ingrediente', 'quantidade']

class SearchForm(forms.Form):
    query = forms.CharField(label='Buscar', max_length=100, required=False)
