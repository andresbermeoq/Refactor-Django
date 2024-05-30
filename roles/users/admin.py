from django.contrib import admin
from .models import Country, Permission, Role, RoleArea, RolePermission, Area

admin.site.register(Country)
admin.site.register(Permission)
admin.site.register(Area)
admin.site.register(Role)
admin.site.register(RoleArea)
admin.site.register(RolePermission)
