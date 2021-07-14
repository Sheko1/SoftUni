from django.http import HttpResponse


def user_group_required(view_func):
    def wrapper(req, *args, **kwargs):
        user = req.user

        if user.is_superuser:
            return view_func(req, *args, **kwargs)

        if not user.is_authenticated:
            return HttpResponse('You must be signed in!')

        user_groups = [g.name for g in user.groups.all()]

        if 'User' not in user_groups:
            return HttpResponse('You must be in "User" group!')

        return view_func(req, *args, **kwargs)

    return wrapper
