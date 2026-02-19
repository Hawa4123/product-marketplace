# products/permissions.py
from rest_framework.permissions import BasePermission

class ProductPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if view.action in ['create', 'update', 'partial_update']:
                return request.user.has_permission('create') or request.user.has_permission('edit')
            if view.action == 'approve':
                return request.user.has_permission('approve')
            if view.action in ['list', 'retrieve']:
                return True
            if view.action == 'destroy':
                return request.user.has_permission('admin')
        return False