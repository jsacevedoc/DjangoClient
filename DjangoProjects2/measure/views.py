from django.shortcuts import render, HttpResponse
import requests

# Create your views here.
#def measure(request):
  #  return render(request, "measure/measure.html")


def cultivo(request):
    if 'codigo' in request.GET:
        codigo = request.GET['codigo']
        latitud = request.GET['latitud']
        longitud = request.GET['longitud']
        producto = request.GET['producto']
        area = request.GET['area']

        # Verifica si el value no esta vacio
        if codigo:
            # Crea el json para realizar la petición POST al Web Service
            args = {'codigo': codigo, 'latitud': latitud, 'longitud': longitud, 'producto': producto, 'area': area}
            print(args)
            response = requests.post('http://p1-cultivo-bck.azurewebsites.net/cultivo/', args)
            # Convierte la respuesta en JSON
            cultivo_json = response.json()

    # Realiza una petición GET al Web Services
    response = requests.get('http://p1-cultivo-bck.azurewebsites.net/cultivo/')
    # Convierte la respuesta en JSON
    cultivo = response.json()
    # Rederiza la respuesta en el template measure
    return render(request, "measure/cultivo.html", {'cultivo': cultivo}) 
