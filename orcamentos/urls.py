from django.urls import path

from . import views

app_name = 'orcamentos'
urlpatterns = [
    path('', views.index, name="index"),
    path('orcamento', views.orcamento, name="orcamento"),
]
