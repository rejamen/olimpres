import os
from base64 import b64decode

from django.test import TestCase
from django.contrib.auth.models import User

from .models import Partner, City


class PartnerTest(TestCase):
    """Testing class for Partners."""

    @classmethod
    def setUpClass(cls):

        super(PartnerTest, cls).setUpClass()

        cls.city = City.objects.create(
            name='Capital City'
        )
        cls.user = User.objects.create(
            username='Test user',
        )
        cls.partner = Partner.objects.create(
            mobile='123456789',
            phone='987654321',
            address1='1st Street',
            address2='Ave. Saint John',
            city_id=cls.city
        )

    def test_001_partner_str(self):
        """----- Test partner str representation."""
        self.assertEqual(
            str(self.partner),
            'Braking test'
        )
        # set one user to partner and
        # check str representation
        self.partner.user_id = self.user
        self.assertEqual(
            str(self.partner),
            'Test user'
        )

    def test_002_get_full_address(self):
        """----- Test Partner full address."""
        self.assertEqual(
            self.partner.get_full_address(),
            '1st Street Ave. Saint John \n Capital City'
        )
