from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Country, Permission, Role, Area, RoleArea, RolePermission
from .serializers import (
    CountrySerializer,
    UserSerializer,
    PermissionSerializer,
    RoleSerializer,
    AreaSerializer,
    RoleAreaSerializer,
    RolePermissionSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


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
