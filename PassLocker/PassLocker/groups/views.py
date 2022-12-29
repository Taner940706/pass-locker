from django.urls import reverse_lazy
from django.views import generic as views

from PassLocker.groups.forms import GroupCreateForm, GroupEditForm, GroupDeleteForm
from PassLocker.groups.models import GroupModel


# Create your views here.


class ListGroupView(views.ListView):
    context_object_name = 'group_list'
    model = GroupModel
    queryset = GroupModel.objects.all()
    template_name = 'groups/details-group-page.html'


class CreateGroupView(views.CreateView):
    template_name = 'groups/create-group-page.html'
    form_class = GroupCreateForm
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super().form_valid(form)


class EditGroupView(views.UpdateView):
    template_name = 'groups/edit-group-page.html'
    form_class = GroupEditForm
    fields = '__all__'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        return super().form_valid(form)


class DeleteGroupView(views.DeleteView):
    template_name = 'groups/delete-group-page.html'
    form_class = GroupDeleteForm
    success_url = reverse_lazy('dashboard')

