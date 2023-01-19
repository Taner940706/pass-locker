from django.core.validators import MinLengthValidator
from django.db import models

from PassLocker.core.validators import validate_only_letters


# Create your models here.
class GroupModel(models.Model):
    GROUP_NAME_MAX_LEN = 30
    GROUP_NAME_MIN_LEN = 5
    group_name = models.CharField(
        max_length=GROUP_NAME_MAX_LEN,
        validators=(MinLengthValidator(GROUP_NAME_MIN_LEN), validate_only_letters, ),
        unique=True,
        null=False,
        blank=False,
    )
    description = models.TextField(
        blank=True,
        null=True,
    )
    created_date = models.DateField(
        auto_now_add=True,
        null=False,
        blank=True,
    )
    updated_date = models.DateField(
        auto_now=True,
        null=False,
        blank=True,
    )

    def __str__(self):
        return self.group_name
