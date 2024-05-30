from django.test import TestCase
from django.contrib.auth.models import User
from .models import Country, Role, Area

class RoleTestCase(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username='test_user', email='test@example.com', password='password'
        )
        self.country_one = Country.objects.create(name='Country One', code='C1')
        self.country_two = Country.objects.create(name='Country Two', code='C2')

    def test_responsible_for_all_roles(self):
        role = Role.objects.create(name='General', country=self.country_one)
        areas = [
            Area.objects.create(name=f"Area {i}", country=self.country_one) for i in range(1, 7)
        ]

        for area in areas:
            role.rolearea_set.create(area=area, is_leader=True)

        self.assertEqual(role.rolearea_set.count(), 6)

    def test_only_role(self):
        test_user = User.objects.create_user(username="user4", password="password4")
        test_role = Role.objects.create(
            name="Responsable", country=self.country_one
        )
        test_user.roles.add(test_role)

        self.assertEqual(test_user.roles.count(), 1)
