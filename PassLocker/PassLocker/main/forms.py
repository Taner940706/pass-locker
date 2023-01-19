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
                Div(

                    Div(

                        Div(

                            Div(
                                Div(

                                    Fieldset(
                                        'Add Locker', 'software_name', 'url', 'username', 'password', 'comment',
                                        'user', 'group',
                                    ),
                                    Div(
                                        Submit('submit', 'Submit', css_class='btn btn-custom btn-lg btn-block'),
                                        css_class='card shadow-2-strong',
                                    ),
                                    css_class='card-body p-5 text-center'
                                ),
                                css_class='card shadow-2-strong'
                            ),
                            css_class='col-12 col-md-8 col-lg-7 col-xl-5'
                        ),
                        css_class='row d-flex justify-content-center align-items-center h-100'
                    ),
                    css_class='container py-5 h-100'
                ),
                css_class='vh-70'
            ),
        )



class MainEditForm(MainBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_id = 'changeLockerForm'
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
            Div(
                Div(

                    Div(

                        Div(

                            Div(
                                Div(

                                    Fieldset(
                                        'Edit Locker', 'software_name', 'url', 'username', 'password', 'comment', 'user', 'group',
                                    ),
                                    Div(
                                        Submit('submit', 'Submit', css_class='btn btn-custom btn-lg btn-block'),
                                        css_class='card shadow-2-strong',
                                    ),
                                    css_class='card-body p-5 text-center'
                                ),
                                css_class='card shadow-2-strong'
                            ),
                            css_class='col-12 col-md-8 col-lg-7 col-xl-5'
                        ),
                        css_class='row d-flex justify-content-center align-items-center h-100'
                    ),
                    css_class='container py-5 h-100'
                ),
                css_class='vh-70'
            ),
        )


class MainDeleteForm(MainBaseForm, DisabledFormMixin):
    disabled_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_action = ""
        self.helper.form_method = 'post'
        self.helper.form_id = 'deleteLockerForm'
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
            Div(
                Div(

                    Div(

                        Div(

                            Div(
                                Div(

                                    Fieldset(
                                        'Delete Locker', 'software_name', 'url', 'username', 'password', 'comment', 'user', 'group',
                                    ),
                                    Div(
                                        Submit('submit', 'Log Me In', css_class='btn btn-custom btn-lg btn-block'),
                                        css_class='card shadow-2-strong',
                                    ),
                                    css_class='card-body p-5 text-center'
                                ),
                                css_class='card shadow-2-strong'
                            ),
                            css_class='col-12 col-md-8 col-lg-7 col-xl-5'
                        ),
                        css_class='row d-flex justify-content-center align-items-center h-100'
                    ),
                    css_class='container py-5 h-100'
                ),
                css_class='vh-50'
            ),
        )

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance
