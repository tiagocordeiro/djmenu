from django.db import models
from django.utils.text import slugify

from core.models import Active, TimeStampedModel
from products.models import Category


# Create your models here.
class Menu(TimeStampedModel, Active):
    name = models.CharField('Nome', max_length=100)
    description = models.TextField('Descrição', blank=True)
    slug = models.SlugField(max_length=255, unique=True, verbose_name="slug",
                            help_text="Preenchido automaticamente, não editar",
                            null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Menu, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.name)


class MenuCategory(TimeStampedModel, Active):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    order = models.PositiveIntegerField('ordem')

    def __str__(self):
        return str(self.category.name + ' - ' + self.menu.name)

    class Meta:
        ordering = ('order',)
        unique_together = [("menu", "category")]
