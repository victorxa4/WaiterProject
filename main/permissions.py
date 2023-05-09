from rest_framework.permissions import BasePermission, SAFE_METHODS

# waiter
class Waiter_FullAccess(BasePermission):
    def has_permission(self, request, view):
        try:
            if request.user.account_type == 'wt':
                pass
                return True
        except:
            return False
class Waiter_ReadOnly(BasePermission):
    def has_permission(self, request, view):
        try:
            if request.user.account_type == 'wt':
                return request.method in SAFE_METHODS
        except:
            return False
        

# kitchen    
class Kitchen_FullAccess(BasePermission):
    def has_permission(self, request, view):
        try:
            if request.user.account_type == 'kt':
                pass
                return True
        except:
            return False
class Kitchen_ReadOnly(BasePermission):
    def has_permission(self, request, view):
        try:
            if request.user.account_type == 'kt':
                return request.method in SAFE_METHODS
        except:
            return False
        
# readonly
class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
    