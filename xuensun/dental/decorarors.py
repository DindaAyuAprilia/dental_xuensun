from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from functools import wraps

def role_required(role):
    """
    Dekorator untuk memastikan hanya user dengan role tertentu yang bisa mengakses view ini.
    """
    def decorator(view_func):
        @wraps(view_func)
        @login_required
        def _wrapped_view(request, *args, **kwargs):
            if request.user.role == role:
                return view_func(request, *args, **kwargs)
            else:
                raise PermissionDenied  # Menghasilkan error 403 jika tidak sesuai role
            
        return _wrapped_view
    return decorator
