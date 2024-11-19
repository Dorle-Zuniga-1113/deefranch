from django.urls import path
from productos_app import views
#cambiar variables a productos
urlpatterns = [
    path("",views.inicio_vista,name="inicio_vista"),
    path("registrarCoordi/",views.registrarCoordi,name="registrarCoordi" ), 
    path("SeleccionarCoordi/<codigo>",views.SeleccionarCoordi,name="SeleccionarCoordi"),
    path("editarCoordi/",views.editarCoordi,name="editarCoordi"),
    path("BorrarCoordi/<codigo>",views.BorrarCoordi,name="BorrarCoordi")
    
]
