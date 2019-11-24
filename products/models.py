from django.db import models

from core.models import TimeStampedModel, Active


class Category(TimeStampedModel, Active):
    name = models.CharField('Categoria', max_length=50, unique=True)
    description = models.TextField('Descrição', blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('name',)
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'


class Product(TimeStampedModel, Active):
    name = models.CharField('Nome', max_length=100)
    description = models.TextField('Descrição', blank=True)
    price = models.DecimalField('Preço', max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('name',)
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"


class Variation(TimeStampedModel, Active):
    name = models.CharField('Variação', max_length=50, unique=True)
    description = models.TextField('Descrição', blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Variação'
        verbose_name_plural = 'Variações'


class ProductVariation(TimeStampedModel, Active):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation = models.ForeignKey(Variation, on_delete=models.CASCADE, null=True)
    price = models.DecimalField('Preço', max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.product.name + ' - ' + self.variation.name + ' - ' + self.price.__str__())

    class Meta:
        ordering = ('product', 'variation', 'price')
        unique_together = [('product', 'variation')]
