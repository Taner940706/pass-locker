from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views import generic as views
from PassLocker.core.get_group import get_group
from PassLocker.core.view_mixin import GetContextAndURLViewMixin
from PassLocker.groups.forms import GroupCreateForm, GroupEditForm, GroupDeleteForm
from PassLocker.groups.models import GroupModel
from PassLocker.main.models import MainModel


# list all groups
class ListGroupView(LoginRequiredMixin, views.ListView):
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


# create group
class CreateGroupView(LoginRequiredMixin, PermissionRequiredMixin, views.CreateView):
    template_name = 'groups/create-group-page.html'
    form_class = GroupCreateForm
    permission_required = 'groups.create_group'

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={'pk': self.request.user.pk})

    def form_valid(self, form):
        messages.warning(self.request, "Successful operation!")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_invalid(self, form):
        messages.error(self.request, "Failed operation!")
        return super().form_invalid(form)


# edit group
class EditGroupView(GetContextAndURLViewMixin, LoginRequiredMixin, PermissionRequiredMixin, views.UpdateView):
    template_name = 'groups/edit-group-page.html'
    model = GroupModel
    form_class = GroupEditForm
    permission_required = 'groups.edit_group'

    def form_valid(self, form):
        messages.warning(self.request, "Successful operation!")
        return super().form_valid(form)


# delete group
class DeleteGroupView(GetContextAndURLViewMixin, LoginRequiredMixin, PermissionRequiredMixin, views.UpdateView):
    template_name = 'groups/delete-group-page.html'
    model = GroupModel
    form_class = GroupDeleteForm
    permission_required = 'groups.delete_group'

    def form_valid(self, form):
        messages.warning(self.request, "Successful operation!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Failed operation!")
        return super().form_invalid(form)
