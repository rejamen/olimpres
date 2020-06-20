import logging
import os
from base64 import b64decode


from django.test import TestCase
from django.contrib.auth.models import User

from .models import Partner, City

from OlimpresTest.models import OlimpresTestData as TestModel

SAVE_FILES_PATH = 'OlimpresTest/media'

# Get an instance of a logger
logger = logging.getLogger(__name__)


class PartnerTest(TestCase):
    """Testing class for Partners."""

    @classmethod
    def setUpClass(cls):

        super(PartnerTest, cls).setUpClass()

        cls.test_obj = TestModel.objects.create()

        cls.city_one = cls.test_obj.create_city()
        cls.user_one = cls.test_obj.create_user()
        # custom values for partner one
        vals = {
            'user_id': cls.user_one
        }
        cls.partner_one = cls.test_obj. \
            create_partner(vals)

    def test_001_partner_str(self):
        """----- Test partner str representation."""
        self.assertEqual(
            str(self.partner_one),
            self.user_one.username
        )

    def test_002_get_full_address(self):
        """----- Test Partner full address."""
        self.assertEqual(
            self.partner_one.get_full_address(),
            '1st Street Ave. Saint John \n Test City'
        )

    def test_03_remove_old_avatar(self):
        """----- Test remove old avatar."""
        # it should delete all files that stars
        # with some given pattern
        pattern = '123_admin'
        try:
            file1 = open(
                '{}/{}.jpg'.format(SAVE_FILES_PATH, pattern),
                'w+'
            )
            file2 = open(
                '{}/{}_xxx.png'.format(SAVE_FILES_PATH, pattern),
                'w+'
            )

            files_before = self. \
                _get_total_files_in_path(pattern, SAVE_FILES_PATH)
            self.assertEqual(files_before, 2)

            # remove old avatars
            self.partner_one. \
                remove_old_avatar(pattern, SAVE_FILES_PATH)

            files_after = self. \
                _get_total_files_in_path(pattern, SAVE_FILES_PATH)
            self.assertEqual(files_after, 0)

        except:
            # TODO create register in Logs App
            logger.error('Remove old avatar TEST returned '
                         'one error.')

    def _get_total_files_in_path(self, pattern, path):
        """Get total of files staring with given pattern.

        :param: str pattern to search files starting with
        :param: str path to search in
        :return: int total of files found
        """
        count = 0
        for root, dirs, files in os.walk(path):
            for name in files:
                if name.startswith(pattern):
                    count += 1
        return count
