from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic as views

from PassLocker.core.get_group import get_group
from PassLocker.core.view_mixin import GetContextAndURLViewMixin
from PassLocker.main.forms import MainCreateForm, MainEditForm, MainDeleteForm
from PassLocker.main.models import MainModel


# Create your views here.


class CreateLockerView(LoginRequiredMixin, views.CreateView):
    template_name = 'main/create-locker-page.html'
    model = MainModel
    form_class = MainCreateForm

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={'pk': self.request.user.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = get_group
        return context

    def form_valid(self, form):
        messages.warning(self.request, "Successful operation!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Failed operation!")
        return super().form_invalid(form)


class EditLockerView(GetContextAndURLViewMixin, LoginRequiredMixin, SuccessMessageMixin, views.UpdateView):
    template_name = 'main/edit-locker-page.html'
    model = MainModel
    form_class = MainEditForm

    def form_valid(self, form):
        messages.warning(self.request, "Successful operation!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Failed operation!")
        return super().form_invalid(form)


class DeleteLockerView(GetContextAndURLViewMixin, LoginRequiredMixin, views.UpdateView):
    template_name = 'main/delete-locker-page.html'
    model = MainModel
    form_class = MainDeleteForm

    def form_valid(self, form):
        messages.warning(self.request, "Successful operation!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Failed operation!")
        return super().form_invalid(form)


