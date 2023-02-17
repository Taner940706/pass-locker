from django.test import TestCase


from PassLocker.main.forms import MainDeleteForm


class MainDeleteFormTests(TestCase):
    def test_delete_main_form_disabled_fields__when_all__expect_ok(self):
        form = MainDeleteForm()
        disabled_fields = {
            name: field.widget.attrs[MainDeleteForm.disabled_attr_name]
            for name, field in form.fields.items()
        }

        self.assertEqual(
            MainDeleteForm.disabled_attr_name,
            disabled_fields['software_name'],
        )
        self.assertEqual(
            MainDeleteForm.disabled_attr_name,
            disabled_fields['url'],
        )
        self.assertEqual(
            MainDeleteForm.disabled_attr_name,
            disabled_fields['username'],
        )
        self.assertEqual(
            MainDeleteForm.disabled_attr_name,
            disabled_fields['password'],
        )
        self.assertEqual(
            MainDeleteForm.disabled_attr_name,
            disabled_fields['comment'],
        )
        self.assertEqual(
            MainDeleteForm.disabled_attr_name,
            disabled_fields['user'],
        )
    from django.test import TestCase


class MainDeleteFormTests(TestCase):
    def test_delete_main_form_disabled_fields__when_all__expect_ok(self):
        form = MainDeleteForm()
        disabled_fields = {
            name: field.widget.attrs[MainDeleteForm.disabled_attr_name]
            for name, field in form.fields.items()
        }

        self.assertEqual(
            MainDeleteForm.disabled_attr_name,
            disabled_fields['software_name'],
        )
        self.assertEqual(
            MainDeleteForm.disabled_attr_name,
            disabled_fields['url'],
        )
        self.assertEqual(
            MainDeleteForm.disabled_attr_name,
            disabled_fields['username'],
        )
        self.assertEqual(
            MainDeleteForm.disabled_attr_name,
            disabled_fields['password'],
        )
        self.assertEqual(
            MainDeleteForm.disabled_attr_name,
            disabled_fields['comment'],
        )
        self.assertEqual(
            MainDeleteForm.disabled_attr_name,
            disabled_fields['user'],
        )
        self.assertEqual(
            MainDeleteForm.disabled_attr_name,
            disabled_fields['group'],
        )
    def test_delete_main_form_disabled_fields__when_software_name_is_disabled__expect_software_name_to_be_disabled(self):
        MainDeleteForm.disabled_fields = ('software_name',)
        form = MainDeleteForm()
        disabled_fields = {
            name: field.widget.attrs[MainDeleteForm.disabled_attr_name]
            for name, field in form.fields.items()
            if MainDeleteForm.disabled_attr_name in field.widget.attrs
        }

        self.assertEqual(
            MainDeleteForm.disabled_attr_name,
            disabled_fields['software_name'],
        )
        self.assertEqual(1, len(disabled_fields))
