import os
import logging

from django.db import models
from django.contrib.auth.models import User


# Get an instance of a logger
logger = logging.getLogger(__name__)

SAVE_FILES_PATH = 'users/avatars'


class Partner(models.Model):
    """Every person in Olimpres is a Partner.

    Proxy model that extends the base data with
    other information.
    """
    
    def set_partner_avatar_name(self, filename):
        """Create a new file for user avatar.
        
        From the uploaded file it takes the name and
        the extension, and creates a new file using the
        user id and the extension.
        
        As result we will have e.g: 123_john.png, where
        123 is the user id and john is user name and 
        png is the extension of uploaded file.
        
        :param str filename: name of uploaded file
        :return str: filename
        """
        ext = filename.split('.')[-1]
        filename = '{}_{}.{}'. \
            format(self.user_id.id, self.user_id.username, ext)
        self.remove_old_avatar('{}_'.format(self.user_id.id))

        return os.path.join(SAVE_FILES_PATH, filename)
    
    def remove_old_avatar(self, pattern, path=SAVE_FILES_PATH):
        """Remove old user avatar in file store.
        
        It search for files that match given pattern
        to delete them. The pattern is all files which
        start with "userId_"

        :param: str pattern to search
        :param: str path: for testing it can use
            a different path.
        """
        try:
            for root, dirs, files in os.walk(path):
                for name in files:
                    if name.startswith(pattern):
                        os.remove('{}/{}'.format(path, name))
        except:
            # TODO Add register in OlimpresLogs app
            logger.error('----- AVATAR deletion ERROR: {} !!!!!!'.format(self.user_id.id))
    
    user_id = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    mobile = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name='Móvil',
        help_text='Móvil de contacto'
    )
    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name='Teléfono',
        help_text='Teléfono de contacto'
    )
    address1 = models.CharField(
        max_length=300,
        blank=True,
        null=True,
        verbose_name='Calle/No.',
    )
    address2 = models.CharField(
        max_length=300,
        blank=True,
        null=True,
        verbose_name='Entre calles/Rpto/otros',
    )
    city_id = models.ForeignKey(
        'City',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name='Ciudad',
    )
    picture = models.ImageField(
        upload_to=set_partner_avatar_name,
        blank=True,
        null=True
    )

    def __str__(self):
        """How this record will be displayed."""
        if self.user_id:
            return self.user_id.username
        return 'No user'

    def get_full_address(self):
        """Get full address for this partner."""
        return '{} {} \n {}'.format(self.address1, self.address2, self.city_id.name)


class City(models.Model):
    """City model for Olimpres."""

    name = models.CharField(
        max_length=100,
        verbose_name='Nombre',
    )

    class Meta:
        verbose_name_plural = 'Ciudades'

    def __str__(self):
        """How this record will be displayed."""
        return self.name
