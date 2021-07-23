from django.http import HttpResponse


class UserGroupRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        user = request.user

        if user.is_superuser:
            return super().dispatch(request, *args, **kwargs)

        if not user.is_authenticated:
            return HttpResponse('You must be signed in!')

        user_groups = [g.name for g in user.groups.all()]

        if 'User' not in user_groups:
            return HttpResponse('You must be in "User" group!')

        return super().dispatch(request, *args, **kwargs)
