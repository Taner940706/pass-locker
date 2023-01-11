from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, Div
from django.contrib.auth import forms as auth_forms, get_user_model
from django.urls import reverse


UserModel = get_user_model()


class UserEditForm(auth_forms.UserChangeForm):
    class Meta:
        model = UserModel
        fields = ('id', 'first_name', 'last_name', 'email', 'department', 'picture')
        field_classes = {'username': auth_forms.UsernameField, }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_id = 'changeUsernameForm'
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
            Div(
                Div(
                    Div(

                        Div(

                            Div(

                                Div(
                                    Div(

                                        Fieldset(
                                            'Edit', 'id', 'first_name', 'last_name', 'email', 'department', 'picture'
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
                css_class='col py-3'
            ),
        )


class UserCreateForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email', 'password1', 'password2')
        field_classes = {'username': auth_forms.UsernameField, }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in ('username', 'email', 'password1', 'password2'):
            self.fields[field].help_text = None
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_id = 'registerForm'
        self.helper.form_action = reverse('register user')
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

                                        'Registration', 'username', 'email', 'password1', 'password2',

                                    ),
                                    Div(
                                        Submit('submit', 'Register', css_class='btn btn-custom btn-lg btn-block'),
                                        css_class='card shadow-2-strong',
                                    ),
                                    css_class='card-body p-5 text-center'
                                ),
                                css_class='card shadow-2-strong'
                            ),
                            css_class='col-12 col-md-8 col-lg-7 col-xl-5'
                        ),
                        css_class='row d-flex justify-content-center align-items-center h-50'
                    ),
                    css_class='container py-5 h-55'
                ),
                css_class='vh-50'
            ),

        )
