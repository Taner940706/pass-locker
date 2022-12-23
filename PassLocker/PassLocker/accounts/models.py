from enum import Enum

from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth import models as auth_model

from PassLocker.core.model_mixins import ChoicesEnumMixin
from PassLocker.core.validators import validate_only_letters


# department choice
class Department(ChoicesEnumMixin, Enum):
    FINANCE = 'Finance'
    IT = 'IT'
    HUMAN_RESOURCES = 'Human resources'
    CUSTOMER_SERVICE = 'Customer service'
    LEGAL = 'Legal'
    SALES = 'Sales'


class JobLevel(ChoicesEnumMixin, Enum):
    INTERN = 'Intern'
    SPECIALIST = 'Specialist'
    SENIOR_SPECIALIST = 'Senior specialist'
    EXPERT_SPECIALIST = 'Expert specialist'
    TEAM_LEADER = 'Team leader'
    MANAGER = 'Manager'
    DIRECTOR = 'Director'


class AppUser(auth_model.AbstractUser):
    MAX_FIRST_NAME_LEN = 30
    MIN_FIRST_NAME = 4
    MAX_LAST_NAME_LEN = 30
    MIN_LAST_NAME = 4

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LEN,
        validators=(
            MinLengthValidator(MIN_FIRST_NAME), validate_only_letters),
    )
    last_name = models.CharField(
        max_length=MAX_LAST_NAME_LEN,
        validators=(
            MinLengthValidator(MIN_LAST_NAME), validate_only_letters),
    )
    email = models.EmailField()
    department = models.TextField(
        choices=Department.choices(),
        null=False,
        blank=False,
    )
    job_level = models.TextField(
        choices=JobLevel.choices(),
        null=False,
        blank=False,
    )
    picture = models.ImageField(upload_to='accounts_photos/')
