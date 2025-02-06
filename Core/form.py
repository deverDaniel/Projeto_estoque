from django.forms import ModelForm
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


