"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
      class Meta(AbstractUser.Meta):
        db_table = 'auth_user'