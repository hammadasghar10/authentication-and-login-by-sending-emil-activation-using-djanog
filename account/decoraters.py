from django.core.exceptions import PermissionDenied
from functools import wraps
from django.shortcuts import redirect

def seller_required(view_func):
    """
    Decorator to allow access only to users with the 'seller' role.
    """
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated or not getattr(request.user, 'is_seller', False):
            raise PermissionDenied("You must be logged in as a seller.")
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def customer_required(view_func):
    """
    Decorator to allow access only to users with the 'customer' role.
    """
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated or getattr(request.user, 'is_seller', False):
            raise PermissionDenied("You must be logged in as a customer.")
        return view_func(request, *args, **kwargs)
    return _wrapped_view
