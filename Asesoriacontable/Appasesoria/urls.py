from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="home"),
    path("ver_servicios", views.ver_servicios, name="servicios"),
    #path("alta_servicio/<nombre>", views.alta_servicio),
    path("clientes",views.clientes, name="clientes"),
    path("Profesional",views.profesional, name="profesional"),
    path("alta_servicio", views.servicio_formulario),
    path("alta_cliente", views.cliente_formulario),
    path("alta_profesional", views.profesional_formulario),
    path("buscar_servicio",views.buscar_servicio),
    path("buscar",views.buscar)
]