from django.views import generic as views

# Create your views here.


class CreateLockerView(views.CreateView):
    template_name = 'main/create-locker-page.html'


class EditLockerView(views.UpdateView):
    template_name = 'main/edit-locker-page.html'


class DeleteLockerView(views.DeleteView):
    template_name = 'main/delete-locker-page.html'