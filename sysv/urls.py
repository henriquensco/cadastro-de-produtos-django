from django.urls import path
from .views import HomePage, CadastarProduto, EditarProduto, DetalhesProduto, DeletarProduto

urlpatterns = [
    path('', HomePage, name='homepage'),
    path('cadastrar-produto/', CadastarProduto, name='addproduct'),
    path('editar-produto/<int:pk>', EditarProduto, name='updateproduct'),
    path('detalhes-produto/<int:pk>', DetalhesProduto, name='productdetail'),
    path('deletar-produto/<int:pk>', DeletarProduto, name='deleteproduct'),
]
