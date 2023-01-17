from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic as views

from PassLocker.core.get_group import get_group
from PassLocker.main.forms import MainCreateForm, MainEditForm, MainDeleteForm
from PassLocker.main.models import MainModel


# Create your views here.


class CreateLockerView(LoginRequiredMixin, views.CreateView):
    template_name = 'main/create-locker-page.html'
    form_class = MainCreateForm
    success_url = reverse_lazy('create locker')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = get_group
        return context

    def form_valid(self, form):
        return super().form_valid(form)


class EditLockerView(LoginRequiredMixin, views.UpdateView):
    template_name = 'main/edit-locker-page.html'
    model = MainModel
    form_class = MainEditForm

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('edit locker', kwargs={'pk': pk})

    def form_valid(self, form):
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = get_group
        return context


class DeleteLockerView(LoginRequiredMixin, views.UpdateView):
    template_name = 'main/delete-locker-page.html'
    model = MainModel
    form_class = MainDeleteForm

    def get_success_url(self):
        return reverse_lazy('create locker')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = get_group
        return context


