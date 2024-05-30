from rest_framework import viewsets

from .models import Area, Country, Permission, Role, RoleArea, RolePermission
from .serializers import (
    AreaSerializer,
    CountrySerializer,
    PermissionSerializer,
    RoleAreaSerializer,
    RolePermissionSerializer,
    RoleSerializer,
)


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer


class RoleAreaViewSet(viewsets.ModelViewSet):
    queryset = RoleArea.objects.all()
    serializer_class = RoleAreaSerializer


class RolePermissionViewSet(viewsets.ModelViewSet):
    queryset = RolePermission.objects.all()
    serializer_class = RolePermissionSerializer
