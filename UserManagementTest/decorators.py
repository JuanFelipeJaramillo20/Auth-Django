from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect

def admin_only(view_func):
    def wrapped_view(request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect('home')  # Redirect to a suitable page for non-admins
        return view_func(request, *args, **kwargs)
    return user_passes_test(lambda u: u.is_authenticated)(wrapped_view)
