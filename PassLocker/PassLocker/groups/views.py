from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views import generic as views

from PassLocker.core.get_group import get_group
from PassLocker.groups.forms import GroupCreateForm, GroupEditForm, GroupDeleteForm
from PassLocker.groups.models import GroupModel
from PassLocker.main.models import MainModel


# Create your views here.


class ListGroupView(LoginRequiredMixin, views.ListView):
    # context_object_name = 'group_list'
    model = GroupModel
    queryset = GroupModel.objects.all()
    template_name = 'groups/list-group-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = get_group
        context['this_group'] = GroupModel.objects.get(pk=self.kwargs.get('pk'))
        context['lockers'] = MainModel.objects.filter(group_id=self.kwargs.get('pk'))
        context['has_perm'] = self.request.user.has_perm('main.change_mainmodel')
        return context


class CreateGroupView(LoginRequiredMixin, PermissionRequiredMixin, views.CreateView):
    template_name = 'groups/create-group-page.html'
    form_class = GroupCreateForm
    success_url = reverse_lazy('create locker')
    permission_required = 'groups.create_group'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = get_group
        return context


class EditGroupView(LoginRequiredMixin, PermissionRequiredMixin, views.UpdateView):
    template_name = 'groups/edit-group-page.html'
    model = GroupModel
    form_class = GroupEditForm
    permission_required = 'groups.edit_group'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('details user', kwargs={'pk': pk})

    def form_valid(self, form):
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = get_group
        return context


class DeleteGroupView(LoginRequiredMixin, PermissionRequiredMixin, views.UpdateView):
    template_name = 'groups/delete-group-page.html'
    model = GroupModel
    form_class = GroupDeleteForm
    permission_required = 'groups.delete_group'

    def get_success_url(self):
        return reverse_lazy('create locker')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = get_group
        return context

