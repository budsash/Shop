from django.contrib import admin
from .models import Category, Product

# Используем декораторы
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    # Автоматически дает url адресу имя в соответствии с полем name
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'available',
                    'created', 'updated']
    list_filter = ['available', 'created', 'updated', 'category']
    list_editable = ['price', 'available'] # Изменяемые поля
    # Автоматически дает url адресу имя в соответствии с полем name
    prepopulated_fields = {'slug': ('name',)}
