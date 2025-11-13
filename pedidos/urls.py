from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('pedidos/', views.variable_list, name='pedidoList'),
    path('pedidocreate/', csrf_exempt(views.variable_create), name='pedidoCreate'),
]