import random

from django.db import models
from django.contrib.auth.models import User

from OlimpresPeople import models as people_models


class OlimpresTestData(models.Model):
    """Testing Class for testing purposes."""

    def generate_random_string(self, n=4):
        """Generate random string of length n.

        :param: int n: length for string otherwise 4 as default
        :return: str
        """
        return ''.join(random.choices('abcdefghijklmnoprstuvwxyz', k=n))

    def create_city(self, vals={}):
        """Create Test City.

        :param: dict vals with values to set.
        :return: City obj
        """
        name = vals.get('name', 'Test City')
        city = people_models.City. \
            objects.create(
                name=name,
            )
        return city

    def create_user(self, vals={}):
        """Create Test User.

        :param: dict vals with values to set.
        :return: User obj
        """
        username = vals.get(
            'username',
            'test_user_{}'.format(
                self.generate_random_string()
            )
        )
        user = User.objects.create(
            username=username,
        )
        return user

    def create_partner(self, vals={}):
        """Create a Partner for working with.

        :param: dict vals with values to set.
        :return: Partner obj
        """
        mobile = vals.get('mobile', '123456789')
        phone = vals.get('phone', '987654321')
        address1 = vals.get('address1', '1st Street')
        address2 = vals.get('address2', 'Ave. Saint John')
        city_id = vals.get('city_id')
        user_id = vals.get('user_id')

        partner = people_models.Partner. \
            objects.create(
                mobile=mobile,
                phone=phone,
                address1=address1,
                address2=address2,
                city_id=city_id or self.create_city(),
                user_id=user_id or self.create_user()
            )
        return partner
