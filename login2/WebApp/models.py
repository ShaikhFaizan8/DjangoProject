# myapp/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class Public(AbstractUser):
    # Your custom fields here

    # Provide unique related_name for groups and user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='public_user_groups',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='public_user_permissions',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )

    def __str__(self):
        return self.username
