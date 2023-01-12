from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic as views

from PassLocker.core.get_group import get_group
from PassLocker.main.forms import MainCreateForm, MainEditForm, MainDeleteForm
from PassLocker.main.models import MainModel


# Create your views here.


class ListLockerView(views.ListView):
    context_object_name = 'locker_list'
    model = MainModel
    queryset = MainModel.objects.all()
    template_name = 'main/list-locker-page.html'


class CreateLockerView(views.CreateView):
    template_name = 'main/create-locker-page.html'
    form_class = MainCreateForm
    success_url = reverse_lazy('login user')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = get_group
        return context

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super().form_valid(form)


class EditLockerView(views.UpdateView):
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


class DeleteLockerView(views.UpdateView):
    template_name = 'main/delete-locker-page.html'
    model = MainModel
    form_class = MainDeleteForm

    def get_success_url(self):
        return reverse_lazy('register user')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = get_group
        return context


