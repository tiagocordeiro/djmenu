from django.db import models


class Category(models.Model):
    name = models.CharField('Categoria', max_length=50, unique=True)
    description = models.TextField('Descrição', blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('name',)
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'


class Product(models.Model):
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


class Variation(models.Model):
    name = models.CharField('Variação', max_length=50, unique=True)
    description = models.TextField('Descrição', blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Variação'
        verbose_name_plural = 'Variações'


class ProductVariation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation = models.ForeignKey(Variation, on_delete=models.CASCADE, null=True)
    price = models.DecimalField('Preço', max_digits=10, decimal_places=2)

    class Meta:
        ordering = ('product', 'variation', 'price')
        unique_together = [('product', 'variation')]
