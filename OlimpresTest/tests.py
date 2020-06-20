from django.test import TestCase
from django.contrib.auth.models import User

from .models import OlimpresTestData as TestModel
from OlimpresPeople import models as people_models


class OlimpresTest(TestCase):
    """Testing shared data for testing."""

    @classmethod
    def setUpClass(cls):

        super(OlimpresTest, cls).setUpClass()

        cls.test_obj = TestModel.objects.create()

        cls.city_one = cls.test_obj. \
            create_city({'name': 'My Test City'})
        cls.user_one = cls.test_obj. \
            create_user()

    def test_001_create_random_string(self):
        """----- Test create random string."""
        # default length is 4
        res = self.test_obj. \
            generate_random_string()
        self.assertEqual(
            len(res),
            4
        )
        # custom length of 10
        res = self.test_obj. \
            generate_random_string(n=10)
        self.assertEqual(
            len(res),
            10
        )

    def test_002_create_city(self):
        """----- Test create city."""
        # check default values
        city_one = self.test_obj.create_city()
        self.assertEqual(
            city_one.name,
            'Test City'
        )
        # check custom values
        vals = {
            'name': 'Test Name'
        }
        city_two = self.test_obj.create_city(vals)
        self.assertEqual(
            city_two.name,
            'Test Name'
        )

    def test_003_create_user(self):
        """----- Test create user."""
        # check custom values
        vals = {
            'username': 'test_user_name'
        }
        user_one = self.test_obj.create_user(vals)
        self.assertEqual(
            user_one.username,
            'test_user_name'
        )
        # check default values
        # expected value is 'test_user_XXXX'
        # four random char at the end
        user_two = self.test_obj.create_user()
        expected = user_two.username.split('_')
        self.assertEqual(
            expected[0],
            'test'
        )
        self.assertEqual(
            expected[1],
            'user'
        )
        self.assertEqual(
            len(expected[2]),
            4
        )

    def test_004_create_partner(self):
        """----- Test create partner."""
        # default values
        partner_one = self.test_obj. \
            create_partner()
        self.assertEqual(
            partner_one.mobile,
            '123456789'
        )
        self.assertEqual(
            partner_one.phone,
            '987654321'
        )
        self.assertEqual(
            partner_one.address1,
            '1st Street'
        )
        self.assertEqual(
            partner_one.address2,
            'Ave. Saint John'
        )
        self.assertTrue(partner_one.city_id)
        self.assertTrue(partner_one.user_id)

        # custom values
        vals = {
            'mobile': '112233445566',
            'phone': '778899',
            'address1': 'Address One',
            'address2': 'Address Two',
            'city_id': self.city_one,
            'user_id': self.user_one,
        }
        partner_two = self.test_obj. \
            create_partner(vals)
        self.assertEqual(
            partner_two.mobile,
            '112233445566'
        )
        self.assertEqual(
            partner_two.phone,
            '778899'
        )
        self.assertEqual(
            partner_two.address1,
            'Address One'
        )
        self.assertEqual(
            partner_two.address2,
            'Address Two'
        )
        self.assertEqual(
            partner_two.city_id,
            self.city_one
        )
        self.assertTrue(
            partner_two.user_id,
            self.user_one
        )
        # check to be sure that city
        # of partner_one and
        # partner_two are different because
        # in first case we did not specify any
        # so the default should be selected, but
        # in case two we specified one.
        self.assertNotEqual(
            partner_one.city_id,
            partner_two.city_id
        )
