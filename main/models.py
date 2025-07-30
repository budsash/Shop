from django.db import models
from django.urls import reverse
class Category(models.Model):
    """Класс для категорий товаров"""
    name = models.CharField(max_length=100, db_index=True) # Имя категории
    slug = models.SlugField(max_length=100, unique=True)  # Штука для Url адреса автоматического

    class Meta:
        ordering = ('name', ) # Сортировка
        verbose_name = 'Категория' # Имя
        verbose_name_plural = 'Категории' # Имя в множественном числе

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("main:product_list_by_category", args=[self.slug])


class Product(models.Model):
    """Класс товаров"""
    # Создаем внешний ключ для связи продуктов с категориями
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)

    name = models.CharField(max_length=100, db_index=True) # Имя продукта
    slug = models.SlugField(max_length=100, unique=100) # Штука для Url адреса автоматического
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True) # Картинка для продукта
    description = models.TextField(blank=True) # Описание продукта
    price = models.DecimalField(max_digits=10, decimal_places=2) # Цена продукта
    available = models.BooleanField(default=True) # Доступность продукта в наличии или нет
    created = models.DateTimeField(auto_now_add=True)  # Дата создания
    updated = models.DateTimeField(auto_now=True) # Дата изменения

    class Meta:
        ordering = ('name', ) # Сортировка

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("main:product_detail", args=[self.id, self.slug])

