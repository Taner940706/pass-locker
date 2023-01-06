from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, HTML, Fieldset
from django import forms
from django.urls import reverse

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


class GroupCreateForm(GroupBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'CreateNewGroupForm'
        self.helper.form_action = reverse('create group')
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            Div(
                HTML(
                    '<h1 class="modal-title fs-5" id="exampleModalLabel"><i class="bi bi-plus-lg"></i> Add Group</h1>'),
                css_class='modal-header'
            ),
            Div(
                Fieldset('', 'group_name', 'description', ),
                css_class='modal-body'
            ),
            Div(
                self.helper.add_input(Submit('submit', 'Submit')),
                css_class='modal-footer'
            )
        )


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
