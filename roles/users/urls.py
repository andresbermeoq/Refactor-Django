from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CountryViewSet,
    PermissionViewSet,
    RoleViewSet,
    AreaViewSet,
    RoleAreaViewSet,
    RolePermissionViewSet,
)

router = DefaultRouter()
router.register(r'countries', CountryViewSet)
router.register(r'permissions', PermissionViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'areas', AreaViewSet)
router.register(r'role-areas', RoleAreaViewSet)
router.register(r'role-permissions', RolePermissionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
