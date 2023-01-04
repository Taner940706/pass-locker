from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

from PassLocker.core.form_mixins import DisabledFormMixin
from PassLocker.groups.models import GroupModel


class GroupBaseForm(forms.ModelForm):
    class Meta:
        model = GroupModel
        fields = '__all__'
        widgets = {
            'group_name': forms.TextInput(
                attrs={
                    'placeholders': 'Group name:'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholders': 'Group name:'
                }
            ),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Submit'))


class GroupCreateForm(GroupBaseForm):
    pass


class GroupEditForm(GroupBaseForm):
    pass


class GroupDeleteForm(GroupBaseForm, DisabledFormMixin):
    disabled_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance
