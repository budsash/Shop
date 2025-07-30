from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    # Создаем путь домашней страницы
    path('', views.product_list, name='product_list'),
    # Фильтрация по категориям
    path('<slug:category_slug>/', views.product_list,
         name='product_list_by_category'),
    # Отдельный продукт
    path('<int:id>/<slug:slug>', views.product_detail,
         name='product_detail')

]