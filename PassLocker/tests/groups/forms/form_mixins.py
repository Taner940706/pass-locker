from django.test import TestCase

from PassLocker.groups.forms import GroupDeleteForm


class GroupDeleteFormTests(TestCase):
    def test_delete_group_form_disabled_fields__when_all__expect_ok(self):
        form = GroupDeleteForm()
        disabled_fields = {
            name: field.widget.attrs[GroupDeleteForm.disabled_attr_name]
            for name, field in form.fields.items()
        }

        self.assertEqual(
            GroupDeleteForm.disabled_attr_name,
            disabled_fields['group_name'],
        )
        self.assertEqual(
            GroupDeleteForm.disabled_attr_name,
            disabled_fields['description'],
        )
    def test_delete_group_form_disabled_fields__when_group_name_is_disabled__expect_group_name_to_be_disabled(self):
        GroupDeleteForm.disabled_fields = ('group_name',)
        form = GroupDeleteForm()
        disabled_fields = {
            name: field.widget.attrs[GroupDeleteForm.disabled_attr_name]
            for name, field in form.fields.items()
            if GroupDeleteForm.disabled_attr_name in field.widget.attrs
        }

        self.assertEqual(
            GroupDeleteForm.disabled_attr_name,
            disabled_fields['group_name'],
        )
        self.assertEqual(1, len(disabled_fields))