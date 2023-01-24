from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, get_user_model, login

from PassLocker.accounts.forms import UserCreateForm, UserEditForm
from PassLocker.core.analyses import count_locker_by_username, count_locker_by_time, count_group_by_time
from PassLocker.core.get_group import get_group
from PassLocker.groups.models import GroupModel
from PassLocker.main.models import MainModel

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


class UserDetailsView(LoginRequiredMixin, views.DetailView):
    template_name = 'accounts/user-details-page.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = get_group
        # context['perm'] = self.request.user.get_all_permissions()
        context['all_groups'] = GroupModel.objects.all().count()
        context['all_lockers'] = MainModel.objects.all().count()
        context['all_user_lockers'] = MainModel.objects.filter(user=self.request.user.pk).count()
        context['count_locker_by_username'] = count_locker_by_username
        context['count_locker_by_time'] = count_locker_by_time
        context['count_group_by_time'] = count_group_by_time
        return context


class UserEditView(LoginRequiredMixin, views.UpdateView):
    template_name = 'accounts/user-edit-page.html'
    model = UserModel
    form_class = UserEditForm
    messages.success = "User was updated successfully"

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={'pk': self.request.user.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = get_group
        return context


class UserDeleteView(LoginRequiredMixin, SuccessMessageMixin, views.DeleteView):
    template_name = 'accounts/user-delete-page.html'
    model = UserModel
    success_message = "User was deleted successfully"

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={'pk': self.request.user.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = get_group
        return context


class SignOutView(auth_views.LogoutView):
    next_page = reverse_lazy('login user')
    messages.success = "User was logged out successfully"


class Handler404(views.TemplateView):
    template_name = '404.html'


class Handler500(views.TemplateView):
    template_name = '500.html'



