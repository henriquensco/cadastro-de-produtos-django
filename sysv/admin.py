from django.contrib import admin
from .models import Produtos

class ProdutosAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'preco', 'descriao', 'codigo', 'imagem']

admin.site.register(Produtos, ProdutosAdmin)