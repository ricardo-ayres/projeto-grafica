from django.shortcuts import render
from .models import Produto

# Create your views here.
from django.http import HttpResponse

def index(request):
    produtos = Produto.objects.order_by('nome')
    context = {'produtos': produtos}
    return render(request, 'orcamentos/index.html', context)

def orcamento(request):
    total = 0
    pedido = []
    for pid in request.POST:
        try:
            produto = Produto.objects.get(pk=pid)
        except:
            # skip iteration if not a product id
            continue

        quantidade = int(request.POST[pid])
        subtotal = produto.preco * quantidade
        item = {
            'produto': produto.nome,
            'preco': produto.preco,
            'quantidade': quantidade,
            'subtotal': subtotal
        }
        pedido.append(item)
        total += subtotal

    context = {'pedido': pedido, 'total': total}
    return render(request, 'orcamentos/orcamento.html', context)
    
