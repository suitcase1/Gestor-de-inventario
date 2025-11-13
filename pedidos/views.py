from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import PedidoForm
from .logic.pedido_logic import get_pedidos, create_pedido
from django.contrib.auth.decorators import login_required
from gestor_de_inventario.auth0backend import getRole


@login_required
def pedido_list(request):
    role = getRole(request)
    if role == "Gerencia Campus":
        pedidos = get_pedidos()
        context = {
            'pedido_list': pedidos
        }
        return render(request, 'Pedido/pedidos.html', context)
    else:
        return HttpResponse("Unauthorized User")


@login_required
def single_pedido(request, id=0):
    pedido = get_pedidos(id)
    context = {
        'pedido': pedido
    }
    return render(request, 'Pedido/pedido.html', context)


@login_required
def pedido_create(request):
    role = getRole(request)
    if role == "Gerencia Campus":
        if request.method == 'POST':
            form = PedidoForm(request.POST)
            if form.is_valid():
                create_pedido(form)
                messages.add_message(request, messages.SUCCESS, 'Successfully created pedido')
                return HttpResponseRedirect(reverse('pedidoCreate'))
            else:
                print(form.errors)
        else:
            form = PedidoForm()
        context = {
            'form': form,
        }
        return render(request, 'Pedido/pedidoCreate.html', context)
    else:
        return HttpResponse("Unauthorized User")
