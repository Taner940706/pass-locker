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
                HTML("""<img src="/static/photos/padlock-no-background.png" class="centerImage" alt="лого">"""),
                Fieldset('Create Group', 'group_name', 'description', ),
                css_class='modal-body'
            ),
            Div(
                self.helper.add_input(Submit('submit', 'Submit')),
                css_class='modal-footer'
            )
        )


class GroupEditForm(GroupBaseForm):
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
                                        'Edit Group', 'group_name', 'description',
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


class GroupDeleteForm(GroupBaseForm, DisabledFormMixin):
    disabled_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_id = 'deleteGroupForm'
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
                                        'Delete Group', 'group_name', 'description',
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

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance
