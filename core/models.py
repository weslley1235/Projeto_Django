from django.db import models

# Create your models here.

class Products (models.Model):
    name = models.CharField('Nome', max_length=100)
    price = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    stock = models.IntegerField('Quantidade em Estoque')

    #A função abaixo é para retornar o name do produto na exibição dentro do painel admin
    def __str__(self):
        return self.name
