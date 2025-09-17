#receitas/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('receita/<int:id>/', views.receita_detail, name = "receita_detail"),
    path('pesquisar/', views.pesquisar_receitas, name='pesquisar_receitas'),
    path('sobre_nos/', views.sobre_nos, name='sobre_nos'),
]