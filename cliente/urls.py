from django.urls import path
from .import views

urlpatterns = [
    path('',views.add_cliente,name='add_cliente_url'),
    path('listar_clientes/',views.listar_clientes,name='listar_clientes'),
    
]