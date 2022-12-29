from django import forms

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
    pass


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
