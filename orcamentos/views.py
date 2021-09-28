from django.shortcuts import render
from .models import Produto

# Create your views here.
from django.http import HttpResponse

def index(request):
    produtos = Produto.objects.order_by('nome')
    context = {'produtos': produtos}
    return render(request, 'orcamentos/index.html', context)
