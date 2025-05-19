# Request - Response (Django/HTTP)

## Landing Page

http://127.0.0.1:8000/
Página de inicio básica.

## Home

http://127.0.0.1:8000/home/ 
Esta página demuestra cómo manejar GET y POST en una sola vista.

## /request

http://127.0.0.1:8000/request/  
Responde por HttpRequest

### /request/app-attributes

http://127.0.0.1:8000/request/app-attributes/ 
Responde con un atributo que fue seteado en la vista.

### /request/middleware

http://127.0.0.1:8000/request/middleware/ 
Responde con un atributo que fue seteado en el Middleware

### /request/querydict

http://127.0.0.1:8000/request/querydict/ 
Responde con un objetos QueryDict

### /request/is-secure
http://127.0.0.1:8000/request/is-secure/ 
Utiliza HttpRequest.is_secure()

## /response

http://127.0.0.1:8000/response/ 
Esto es un HttpResponse básico.

### /response/subclasses

http://127.0.0.1:8000/response/subclasses/ 
Este es un HttpResponse con encabezados

### /response/json

http://127.0.0.1:8000/response/json/ 
Responde con JSON

### /response/streaming

http://127.0.0.1:8000/response/streaming/ 
Responde con una secuencia de streaming

### /response/file

http://127.0.0.1:8000/response/file/ 
Responde con algún recurso al servidor (archivo)

### /response/base

http://127.0.0.1:8000/response/base/ 
Responde utilizado HttpResponseBase