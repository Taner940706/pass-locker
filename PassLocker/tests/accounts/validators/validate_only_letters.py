from unittest import TestCase

from django.core.exceptions import ValidationError

from PassLocker.core.validators import validate_only_letters


class OnlyLetterValidator(TestCase):
    def test_only_letters_validator__when_valid__expect_ok(self):
        validate_only_letters('Taner')

    def test_only_letters_validator__when_contains_digits__expect_exception(self):
        with self.assertRaises(ValidationError) as context:
            validate_only_letters('Taner940706')
        self.assertIsNotNone(context.exception)