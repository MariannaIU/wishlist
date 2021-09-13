from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    """
    docstring
    Таблица 'Товар'

    id(Django) автоматом добавит
    Название товара
    Ссылка на товар
    Цена товара
    Дата и время создания записи
    """
    title = models.CharField(max_length=120, verbose_name='Название')
    link = models.URLField(verbose_name='Ссылка')
    price = models.IntegerField(verbose_name='Цена')
    create_at  = models.DateTimeField(auto_now_add=True, auto_created=True)

    def __str__(self):
        return self.title



class WishList(models.Model):
    """
    Таблица "Лист любимых подарков"
    id
    owner
    products - ManyToMany
    is_hidden - bool
    """
    title = models.CharField(max_length=120)
    product = models.ManyToManyField(Product)
    is_hidden = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

