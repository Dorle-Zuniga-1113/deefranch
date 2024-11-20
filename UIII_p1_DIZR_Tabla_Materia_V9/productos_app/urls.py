from django.urls import path
from productos_app import views
#cambiar variables a productos
urlpatterns = [
    path("",views.inicio_vista,name="inicio_vista"),
    path("registrarproducto/",views.registrarProducto,name="registrarproducto" ), 
    path("seleccionarproducto/<codigo>",views.SeleccionarProducto,name="seleccionarproducto"),
    path("editarproducto/",views.EditarProducto,name="editarproducto"),
    path("borrarproducto/<codigo>",views.BorrarProducto,name="borrarproducto")
    
]
