from django.views import generic as views

# Create your views here.


class ListGroupView(views.ListView):
    template_name = 'groups/details-group-page.html'


class CreateGroupView(views.CreateView):
    template_name = 'groups/create-group-page.html'


class EditGroupView(views.UpdateView):
    template_name = 'groups/edit-group-page.html'


class DeleteGroupView(views.DeleteView):
    template_name = 'groups/delete-group-page.html'