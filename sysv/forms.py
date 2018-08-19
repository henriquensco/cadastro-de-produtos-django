from django import forms
from .models import Produtos

class ProdutosForm(forms.ModelForm):
    class Meta:
        model = Produtos
        fields = ['titulo', 'preco', 'descriao', 'codigo', 'imagem']
        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder':'Titulo', 'class': 'form-control form-control-lg'}),
            'nome_produto': forms.TextInput(attrs={'placeholder':'Nome do Produto', 'class': 'form-control form-control-lg'}),
            'descriao': forms.Textarea(attrs={'placeholder':'Descricao', 'class': 'form-control form-control-lg'}),
            'preco': forms.TextInput(attrs={'placeholder':'Preco', 'class': 'form-control form-control-lg'}),
            'codigo': forms.TextInput(attrs={'placeholder':'Codigo de Barras', 'class': 'form-control form-control-lg','autocomplete':'off'}),
            'imagem': forms.FileInput(attrs={'id':'validatedCustomFile'})
        }