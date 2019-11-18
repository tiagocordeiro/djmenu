from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField('Nome', max_length=100)
    description = models.TextField('Descrição')
    price = models.DecimalField('Preço', max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('name',)
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"


class Category(models.Model):
    name = models.CharField('Categoria', max_length=50, unique=True)
    description = models.TextField('Descrição', blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('name',)
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"


class Ingredient(models.Model):
    name = models.CharField('Ingrediente', max_length=50, unique=True)
    description = models.TextField('Descrição', blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('name',)
        verbose_name = "Ingrediente"
        verbose_name_plural = "Ingredientes"


class Variation(models.Model):
    name = models.CharField('Variação', max_length=50, unique=True)
    description = models.TextField('Descrição', blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('name',)
        verbose_name = "Variação"
        verbose_name_plural = "Variações"


class ProductVariation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation = models.ForeignKey(Variation, on_delete=models.CASCADE)
    price = models.DecimalField('Preço', max_digits=10, decimal_places=2)

    class Meta:
        ordering = ('product', 'variation', 'price')
        unique_together = [("product", "variation")]


class ProductIngredient(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

    class Meta:
        ordering = ('product', 'ingredient')
        unique_together = [("product", "ingredient")]


class ProductCategory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ('category', 'product')
        unique_together = [("product", "category")]
