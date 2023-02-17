from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models
from PassLocker.core.validators import validate_only_letters
from PassLocker.groups.models import GroupModel

# Create your models here.

UserModel = get_user_model()


class MainModel(models.Model):
    SOFTWARE_NAME_MAX_LEN = 30
    SOFTWARE_NAME_MIN_LEN = 5
    USERNAME_MAX_LEN = 15
    USERNAME_MIN_LEN = 4
    PASSWORD_NAME_MAX_LEN = 20
    PASSWORD_NAME_MIN_LEN = 8

    software_name = models.CharField(
        max_length=SOFTWARE_NAME_MAX_LEN,
        validators=(MinLengthValidator(SOFTWARE_NAME_MIN_LEN), validate_only_letters,),
        null=False,
        blank=False,

    )
    url = models.URLField(
        null=False,
        blank=False,
    )
    username = models.CharField(
        max_length=USERNAME_MAX_LEN,
        validators=(MinLengthValidator(USERNAME_MIN_LEN),),
        null=False,
        blank=False,

    )
    password = models.CharField(
        max_length=PASSWORD_NAME_MAX_LEN,
        validators=(MinLengthValidator(PASSWORD_NAME_MIN_LEN),),
        null=False,
        blank=False,
    )
    comment = models.TextField(
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
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
    group = models.ForeignKey(
        GroupModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.group
