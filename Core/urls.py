from django.contrib import admin
from django.urls import path
from Core.views import home,ingredientes, produtos, Ingrediente_novo, Produto_novo, adicionar_ingrediente

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name = 'core_home'),
    path("ingredientes/", ingredientes, name = "core_ingredientes"),
    path("produtos/", produtos, name = "core_produtos"),
    path('adicionar_ingrediente/<int:id>', adicionar_ingrediente, name='core_adicionar_ingrediente'),

    path("ingrediente-novo/", Ingrediente_novo, name = "core_ingrediente_novo"),
    path("produto-novo/", Produto_novo, name = "core_produto_novo"),
]
