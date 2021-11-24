from django.urls import path

from . import views

app_name = 'orcamentos'
urlpatterns = [
    path('', views.index, name="index"),
    path('catalogo/', views.catalogo, name="catalogo"),
    path('orcamento/', views.orcamento, name="orcamento"),
]
