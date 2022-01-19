from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Проверка наличия прав редактирования и удаления объектов."""

    def permission_to_object(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
