from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, get_user_model, login

from PassLocker.accounts.forms import UserCreateForm, UserEditForm
from PassLocker.core.get_group import get_group
from PassLocker.groups.models import GroupModel

UserModel = get_user_model()


class SignInView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'


class SignUpView(views.CreateView):
    template_name = 'accounts/register-page.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('login user')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class UserDetailsView(views.DetailView):
    template_name = 'accounts/user-details-page.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = get_group
        return context


class UserEditView(views.UpdateView):
    template_name = 'accounts/user-edit-page.html'
    model = UserModel
    form_class = UserEditForm

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('edit user', kwargs={'pk': pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = get_group
        return context


class UserDeleteView(views.DeleteView):
    template_name = 'accounts/user-delete-page.html'
    model = UserModel
    success_url = reverse_lazy('register user')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = get_group
        return context


class SignOutView(auth_views.LogoutView):
    next_page = reverse_lazy('login user')



