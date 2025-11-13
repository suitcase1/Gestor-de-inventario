from ..models import Pedido

def get_pedidos():
    queryset = Pedido.objects.all()
    return queryset

def create_pedido(form):
    pedido = form.save()
    pedido.save()
    return pedido
