from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic as views

from PassLocker.core.get_group import get_group
from PassLocker.groups.forms import GroupCreateForm, GroupEditForm, GroupDeleteForm
from PassLocker.groups.models import GroupModel
from PassLocker.main.models import MainModel


# Create your views here.


class ListGroupView(views.ListView):
    # context_object_name = 'group_list'
    model = GroupModel
    queryset = GroupModel.objects.all()
    template_name = 'groups/list-group-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = get_group
        context['this_group'] = GroupModel.objects.get(pk=self.kwargs.get('pk'))
        context['lockers'] = MainModel.objects.get(group_id=self.kwargs.get('pk'))
        return context


class CreateGroupView(views.CreateView):
    template_name = 'groups/create-group-page.html'
    form_class = GroupCreateForm
    success_url = reverse_lazy('login user')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = get_group
        return context


class EditGroupView(views.UpdateView):
    template_name = 'groups/edit-group-page.html'
    model = GroupModel
    form_class = GroupEditForm
    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('edit group', kwargs={'pk': pk})

    def form_valid(self, form):
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = get_group
        return context


class DeleteGroupView(views.UpdateView):
    template_name = 'groups/delete-group-page.html'
    model = GroupModel
    form_class = GroupDeleteForm

    def get_success_url(self):
        return reverse_lazy('register user')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = get_group
        return context

