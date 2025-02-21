from django.contrib import admin
from django.urls import path
from Core.views import home,ingredientes, produtos, Ingrediente_novo, Produto_novo,\
    adicionar_ingrediente, Atualiza_ingrediente, Deletar_ingrediente, Atualiza_Produto_Ingrediente,\
    Deletar_Produto_Ingrediente

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name = 'core_home'),
    path("ingredientes/", ingredientes, name = "core_ingredientes"),
    path("produtos/", produtos, name = "core_produtos"),

    path('adicionar_ingrediente/<int:id>', adicionar_ingrediente, name='core_adicionar_ingrediente'),
    path('adicionar_quantidade/<int:id>/<int:quantidade>', adicionar_ingrediente, name='core_adicionar_quantidade'),
    path("ingrediente-novo/", Ingrediente_novo, name = "core_ingrediente_novo"),
    path("produto-novo/", Produto_novo, name = "core_produto_novo"),


    path("atualiza-ingrediente/<int:id>", Atualiza_ingrediente, name = "core_update_ingrediente"),
    path("atualiza-produto_ingrediente/<int:produto_id>/<int:ingrediente_id>/", Atualiza_Produto_Ingrediente, name = "core_update_produto_ingrediente"),

    path("deletar-ingrediente/<int:id>", Deletar_ingrediente , name = "core_deletar_ingrediente"),
    path("deletar-ingrediente/<int:produto_id>/<int:ingrediente_id>/", Deletar_Produto_Ingrediente , name = "core_deletar_produto_ingrediente"),
]
