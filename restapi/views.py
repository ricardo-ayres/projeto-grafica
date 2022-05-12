#from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from .serializers import ProdutoSerializer
from orcamentos.models import Produto

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all().order_by('nome')
    serializer_class = ProdutoSerializer
