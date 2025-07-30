from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
# Функция для отображения домашней страницы
def product_list(request, category_slug=None):
    categories = Category.objects.all() # Достаем все категории
    products = Product.objects.filter(available=True) # Достаем ДОСТУПНЫЕ продукты (available=True)

    category = None
    # Условие для фильтрации
    if category_slug:
        # Присваиваем url
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'main/product/list.html', context={'category': category,
                                                              'categories': categories,
                                                              'products': products})

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    related_products = Product.objects.filter(category=product.category,
                                              available=True).exclude(id=product.id)[:4]
    cart_product_form = CartAddProductForm()


    return render(request, 'main/product/detail.html', context={'product': product,
                                                                'related_products': related_products,
                                                                'cart_product_form': cart_product_form})

