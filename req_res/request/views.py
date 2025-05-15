from django.http import HttpResponse, JsonResponse, StreamingHttpResponse, FileResponse
from django.http.response import HttpResponseBase
from django.shortcuts import render
import time, os

class MiRespuestaPersonalizada(HttpResponseBase):
    def __init__(self, contenido, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.content = contenido
        self.status_code = 202
        self['X-Mensaje'] = 'Respuesta personalizada usando HttpResponseBase'

# Create your views here.
def index(request):
    return render(request, 'request/landing.html')

def home(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        #mensaje = request.POST.get('mensaje')
        
        return HttpResponse(f"Gracias por tu mensaje, {nombre}!\nTu mensaje: {memoryview}")
    
    return render(request, 'request/index.html')

# /request/{algo}

def req(request):
    metodo = request.method
    path = request.path
    user_agent = request.headers.get('User-Agent', 'Desconocido')
    
    respuesta = f"""
        Método: {metodo}<br>
        Ruta: {path}<br>
        User-Agent: {user_agent}
    """
    
    return HttpResponse(respuesta)

def app_attributes(request):
    # Seteamos un atributo personalizado en el objeto request
    request.mi_atributo = "¡Hola! Este es un atributo personalizado."
    
    # Lo usamos en la respuesta
    return HttpResponse(f"El valor del atributo es: {request.mi_atributo}")

def middleware(request):
    valor = getattr(request, 'desde_middleware', 'No hay atributo')
    return HttpResponse(f"Atributo desde middleware: {valor}")

def querydict(request):
    query_params = request.GET.dict()  # Esto es un QueryDict y lo transformamos a un diccionario
    
    # Lo mostramos como JSON
    return JsonResponse(query_params)

def is_secure(request):
    if request.is_secure():
        mensaje = "La conexión es segura (HTTPS)."
    else:
        mensaje = "La conexión NO es segura (probablemente HTTP)."
    return HttpResponse(mensaje)

# /response/{algo}

def res(request):
    return HttpResponse("Hola desde Django con HttpResponse")

def subclasses(request):
    response = HttpResponse("Respuesta con encabezados personalizados.")
    response['X-Curso'] = 'Django Básico'
    response['X-Autor'] = 'Luis'
    response['Cache-Control'] = 'no-store'
    return response

def json(request):
    data = {
        'mensaje': 'Hola desde Django',
        'autor': 'Luis',
        'Materia': 'Practica Profesionalizante 1',
    }

    return JsonResponse(data)

def streaming(request):
    def generador():
        yield "Inicio del stream\n"
        for i in range(5):
            yield f"Línea {i + 1}\n"
            time.sleep(1)  # Simula un retardo, como si viniera de una fuente externa
        yield "Fin del stream\n"

    return StreamingHttpResponse(generador(), content_type="text/plain")

def file(request):
    archivo_path = os.path.join('media', 'Linux.pdf')  # Ruta del archivo en el servidor
    try:
        # Abrimos el archivo en modo binario
        archivo = open(archivo_path, 'rb')
        response = FileResponse(archivo, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="archivo.pdf"'
        return response
    except FileNotFoundError:
        return HttpResponse("Archivo no encontrado", status=404)

def base(request):
    return MiRespuestaPersonalizada("Este contenido viene de una clase que hereda de HttpResponseBase.")