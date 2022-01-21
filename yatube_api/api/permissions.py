from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Проверка наличия прав редактирования и удаления объектов."""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
