from django.shortcuts import redirect
from django.urls import resolve

class UserProfileAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Si el usuario no está autenticado, dejamos pasar el request sin hacer ninguna verificación.
        if not request.user.is_authenticated:
            return self.get_response(request)

        # Verificar si el usuario pertenece al grupo del director.
        # is_director = request.user.groups.filter(name='Director').exists()
        # # si quien esta logeado es el director se acepta la peticion
        # if is_director:
        #     return self.get_response(request)

        # Obtener el usuario solicitado desde la URL.
        requested_user_id = None
        try:
            kwargs = resolve(request.path).kwargs
            requested_user_id = int(kwargs.get('user_id', None))
        except (ValueError, KeyError, TypeError):
            pass

        # Verificar si el usuario solicitado es el mismo que el usuario autenticado.
        if requested_user_id is not None and requested_user_id != request.user.id:
            return redirect('/authentication/error_404/')  #redirigir si el acceso es denegado.

        return self.get_response(request)
