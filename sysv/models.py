from django.db import models


class Produtos(models.Model):
    titulo = models.CharField(max_length=100)
    preco = models.CharField(max_length=30)
    imagem = models.ImageField(upload_to='produtos/', blank=True)
    descriao = models.CharField(max_length=200)
    codigo = models.CharField(max_length=100)

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return self.titulo