from django.db import models
from products.models import Category


# Create your models here.
class Menu(models.Model):
    name = models.CharField('Nome', max_length=100)
    description = models.TextField('Descrição', blank=True)


class MenuCategory(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    order = models.PositiveIntegerField('ordem')

    class Meta:
        ordering = ('order', )
        unique_together = [("menu", "category")]
