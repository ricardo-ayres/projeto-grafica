from django.shortcuts import render
from .models import Produto

from decimal import Decimal

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'orcamentos/index.html')

def catalogo(request):
    produtos = Produto.objects.order_by('nome')
    context = {'produtos': produtos}
    return render(request, 'orcamentos/catalogo.html', context)

def orcamento(request):
    total = 0
    pedido = []
    for pid in request.POST:
        try:
            produto = Produto.objects.get(pk=pid)
        except:
            # skip iteration if not a product id
            continue

        quantidade = Decimal(request.POST[pid])
        if quantidade == Decimal(0): continue

        subtotal = produto.preco * quantidade
        item = {
            'produto': produto,
            'quantidade': quantidade,
            'subtotal': subtotal
        }
        pedido.append(item)
        total += subtotal

    context = {'pedido': pedido, 'total': total}
    return render(request, 'orcamentos/orcamento.html', context)

def app(request):
    return render(request, 'app/app.html')
