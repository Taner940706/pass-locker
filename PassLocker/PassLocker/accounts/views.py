from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, get_user_model, login

from PassLocker.accounts.forms import UserCreateForm, UserEditForm, UserDeleteForm
from PassLocker.core.view_mixin import GetContextAndURLViewMixin


UserModel = get_user_model()


class SignInView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'

    def form_invalid(self, form):
        messages.error(self.request, "Username and/or password is incorrect!")
        return super().form_invalid(form)


class SignUpView(views.CreateView):
    template_name = 'accounts/register-page.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('login user')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result

    def form_invalid(self, form):
        if form['password1'].value() != form['password2'].value():
            messages.error(self.request, "Passwords doesn't match")
        else:
            messages.error(self.request, "Username exist!!")
        return super().form_invalid(form)


class UserDetailsView(GetContextAndURLViewMixin, LoginRequiredMixin, views.DetailView):
    template_name = 'accounts/user-details-page.html'
    model = UserModel


class UserEditView(GetContextAndURLViewMixin, LoginRequiredMixin, SuccessMessageMixin, views.UpdateView):
    template_name = 'accounts/user-edit-page.html'
    model = UserModel
    form_class = UserEditForm
    # success_message = "User was updated successfully"

    def form_invalid(self, form):
        messages.error(self.request, "Failed operation!")
        return super().form_invalid(form)



# class UserDeleteView(GetContextAndURLViewMixin, LoginRequiredMixin, SuccessMessageMixin, views.DeleteView):
#     template_name = 'accounts/user-delete-page.html'
#     model = UserModel
#     success_message = "User was deleted successfully"


class UserDeleteView(GetContextAndURLViewMixin, LoginRequiredMixin, SuccessMessageMixin, views.UpdateView):

    template_name = 'accounts/user-delete-page.html'

    form_class = UserDeleteForm
    model = UserModel
    success_message = "User was deleted successfully"


class SignOutView(auth_views.LogoutView):
    next_page = reverse_lazy('login user')
    messages.success = "User was logged out successfully"


class Handler404(views.TemplateView):
    template_name = '404.html'


class Handler500(views.TemplateView):
    template_name = '500.html'



