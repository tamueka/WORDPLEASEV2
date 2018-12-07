from rest_framework.permissions import BasePermission


class BlogPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        #define si el usuario aunteticvado puede realizar la accion sobre el objeto ob
        #leer, actualizar o borrar
        #cualquier usuario puede leer o el usuario es propietario del blog o superusuario admin
        return request.method == 'GET' or obj.usuario == request.user or request.user.is_superuser

