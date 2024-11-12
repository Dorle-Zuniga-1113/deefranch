from django.urls import path
from coordinador_app import views

urlpatterns = [
    path("",views.inicio_vista,name="inicio_vista"),
    path("registrarMateria/",views.registrarMateria,name="registrarMateria" ), 
    path("SeleccionarMateria/<codigo>",views.SeleccionarMateria,name="SeleccionarMateria"),
    path("editarMateria/<codigo>",views.editarMateria,name="editarMateria"),
    path("BorrarMateria/<codigo>",views.BorrarMateria,name="BorrarMateria")
    
]
