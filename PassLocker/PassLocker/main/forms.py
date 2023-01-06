from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Fieldset, Div, Layout, HTML
from django import forms
from django.urls import reverse

from PassLocker.core.form_mixins import DisabledFormMixin
from PassLocker.main.models import MainModel


class MainBaseForm(forms.ModelForm):
    class Meta:
        model = MainModel
        fields = '__all__'
        widgets = {
            'software_name': forms.TextInput(
                attrs={
                    'placeholders': 'Software name:'
                }
            ),
            'url': forms.URLInput(
                attrs={
                    'placeholders': 'URL:'
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'placeholders': 'Username:'
                }
            ),
            'password': forms.TextInput(
                attrs={
                    'placeholders': 'Password:'
                }
            ),
            'comment': forms.Textarea(
                attrs={
                    'placeholders': 'URL:'
                }
            ),
            'user': forms.TextInput(
                attrs={
                    'placeholders': 'User:'
                }
            ),
            'group': forms.TextInput(
                attrs={
                    'placeholders': 'Group:'
                }
            ),
        }



class MainCreateForm(MainBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'CreateNewLockerForm'
        self.helper.form_action = reverse('create locker')
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            Div(
                HTML('<h1 class="modal-title fs-5" id="exampleModalLabel"><i class="bi bi-plus-lg"></i> Add Locker</h1>'),
                css_class='modal-header'
            ),
            Div(
                Fieldset('', 'software_name', 'url', 'username', 'password', 'comment', 'user', 'group',),
                css_class='modal-body'
            ),
            Div(
                self.helper.add_input(Submit('submit', 'Submit')),
                css_class='modal-footer'
            )
        )



class MainEditForm(MainBaseForm):
    pass


class MainDeleteForm(MainBaseForm, DisabledFormMixin):
    disabled_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance
