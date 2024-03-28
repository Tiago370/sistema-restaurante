from django.urls import path
from . import views

urlpatterns = [
    path('produtos/', views.produtos, name='produtos'),
    path('produtos/delete/<int:id>', views.delete_produto, name='delete_produto'),
]