from django.shortcuts import redirect
from django.contrib import messages


def admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_staff:
            return view_func(request, *args, **kwargs)
        else:
            messages.error(request, 'شما دسترسی به این بخش ندارید.')
            return redirect('members:course_list')
    return wrapper