from django.shortcuts import render,redirect
from .models import Coordinador
# Create your views here.

def inicio_vista(request):
    loscoordis=Coordinador.objects.all()

    return render(request,"gestionarCoordinador.html",{"loscoordis":loscoordis})
    
def registrarCoordi(request):
    codigo=request.POST["txtcod"]
    nombre=request.POST["txtnombre"]
    zona=request.POST["txtzona"]
    direccion=request.POST["txtdire"]
    apellidos=request.POST["txtapell"]
    sueldo=request.POST["numsueldo"]
    

    guardarcoordi=Coordinador.objects.create(codigo=codigo,nombre=nombre,zona=zona,direccion=direccion,apellidos=apellidos,sueldo=sueldo)
    return redirect("/")

def SeleccionarCoordi(request,codigo):
    infcoor=Coordinador.objects.get(codigo=codigo)
    return render(request,"editarcoordi.html",{"loscoordis":infcoor})
    
def editarCoordi(request):
    codigo = request.POST["txtcod"]
    try:
        infcoor = Coordinador.objects.get(codigo=codigo)
        infcoor.nombre = request.POST["txtnombre"]
        infcoor.zona = request.POST["txtzona"]
        infcoor.direccion = request.POST["txtdire"]
        infcoor.apellidos = request.POST["txtapell"]
        infcoor.sueldo = request.POST["numsueldo"]
        infcoor.save()
    except Coordinador.DoesNotExist:
        # Manejar el caso de un código no válido
        pass
    return redirect("/")


def BorrarCoordi(request, codigo):
    try:
        infcoor = Coordinador.objects.get(codigo=codigo)
        infcoor.delete()
    except Coordinador.DoesNotExist:
        # Manejar el caso de un código no válido
        pass
    return redirect("/")
