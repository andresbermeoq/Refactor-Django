from django.db import models
from django.contrib.auth.models import User


class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=3, unique=True)
    def __str__(self) -> str:
        return self.name

class Permission(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='roles', blank=True)
    is_clave_role = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name
class Area(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
class RoleArea(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    is_leader = models.BooleanField(default=False)

    class Meta:
        unique_together = ('role', 'area')

class RolePermission(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('role', 'permission')
