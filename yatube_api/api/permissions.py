from rest_framework.permissions import BasePermission


class IsAuthorOrReadOnly(BasePermission):
    """Проверка наличия прав редактирования и удаления объектов."""

    def permission_to_object(self, request, view, obj):
        return (
            (request.method in ('GET', 'POST')) or (obj.author == request.user)
        )
