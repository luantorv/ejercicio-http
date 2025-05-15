class AtributoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Seteamos el atributo antes de que llegue a la vista
        request.desde_middleware = "Este valor vino del middleware."
        return self.get_response(request)
