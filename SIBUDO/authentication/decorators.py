from django.contrib.auth.decorators import user_passes_test

def group_required(group_names):
    def decorator(view_func):
        decorated_view_func = user_passes_test(
            lambda user: user.groups.filter(name__in=group_names).exists(),
            login_url='/',  # redirecciona al home
            # login_url='/error_404/',  # redirecciona a pagina de error
        )(view_func)
        return decorated_view_func
    return decorator