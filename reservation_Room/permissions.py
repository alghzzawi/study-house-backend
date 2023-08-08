from rest_framework.permissions import BasePermission, SAFE_METHODS

# class OwnerOrAdminOnly(BasePermission):
#     def has_permission(self, request, view):
#         if request.method in SAFE_METHODS:
#             return True
#         return request.user.is_authenticated

    # def has_object_permission(self, request, view, obj):
    #     if request.user.is_superuser or request.user.Is_employee:
    #         # Admin can see all reservations
    #         return True

    #     return obj.user_ID  == request.user if request.method != 'POST' else True

class OnlyAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True

        return request.method in SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser