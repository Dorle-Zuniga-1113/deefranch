from django.shortcuts import render,redirect
from .models import Coordinador
# Create your views here.

def inicio_vista(request):
    loscoordis=Coordinador.objects.all()

    return render(request,"gestionarMateria.html",{"loscoordis":loscoordis})
    
def registrarMateria(request):
    cod_coordinador=request.POST["txtcod"]
    nombre=request.POST["txtnombre"]
    zona=request.POST["txtzona"]
    direccion=request.POST["txtdire"]
    apellidos=request.POST["txtapell"]
    sueldo=request.POST["numsueldo"]
    

    guardarcoordi=Coordinador.objects.create(cod_coordinador=cod_coordinador,nombre=nombre,zona=zona,direccion=direccion,apellidos=apellidos,sueldo=sueldo)
    return redirect("/")

def SeleccionarMateria(request,codigo):
    infcoor=Coordinador.objects.get(codigo=codigo)
    return render(request,"editarmateria.html",{"loscoordis":infcoor})
    
def editarMateria(request):
    cod_coordinador=request.POST["txtcod"]
    nombre=request.POST["txtnombre"]
    zona=request.POST["txtzona"]
    direccion=request.POST["txtdire"]
    apellidos=request.POST["txtapell"]
    sueldo=request.POST["numsueldo"]
    infcoor=Coordinador.objects.get(codigo=cod_coordinador)
    infcoor.nombre=nombre
    infcoor.cod_coordinador=cod_coordinador
    infcoor.zona=zona
    infcoor.direccion=direccion
    infcoor.apellidos=apellidos
    infcoor.sueldo=sueldo

    infcoor.save()
    return redirect("/")

def BorrarMateria(request,codigo):
    infcoor=Coordinador.objects.get(codigo=codigo)
    infcoor.delete()



    return redirect("/")