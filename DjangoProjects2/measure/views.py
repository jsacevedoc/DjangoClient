from django.shortcuts import render, HttpResponse
import requests

# Create your views here.
#def measure(request):
  #  return render(request, "measure/measure.html")

def measure(request):
    # Verifica si hay un parámetro value en la petición GET
    if 'value' in request.GET:
        value = request.GET['value']
        # Verifica si el value no esta vacio
        if value:
            # Crea el json para realizar la petición POST al Web Service
            args = {'type': 'Grados', 'value': value}
            response = requests.post('http://127.0.0.1:8000/temphum/', args)
            # Convierte la respuesta en JSON
            measure_json = response.json()

    # Realiza una petición GET al Web Services
    response = requests.get('http://127.0.0.1:8000/temphum/')
    # Convierte la respuesta en JSON
    measures = response.json()
    # Rederiza la respuesta en el template measure
    return render(request, "measure/measure.html", {'measures': measures})

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
            response = requests.post('http://127.0.0.1:8000/cultivo/', args)
            # Convierte la respuesta en JSON
            cultivo_json = response.json()

    # Realiza una petición GET al Web Services
    response = requests.get('http://127.0.0.1:8000/cultivo/')
    # Convierte la respuesta en JSON
    cultivo = response.json()
    # Rederiza la respuesta en el template measure
    return render(request, "measure/cultivo.html", {'cultivo': cultivo}) 
