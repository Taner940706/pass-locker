from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic as views
from PassLocker.core.analyses import count_locker_by_username, count_locker_by_time, count_group_by_time
from PassLocker.core.get_group import get_group
from PassLocker.groups.models import GroupModel
from PassLocker.main.models import MainModel


class GetContextAndURLViewMixin(views.DetailView):

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = get_group
        context['this_group'] = GroupModel.objects.filter(pk=self.kwargs.get('pk'))
        context['lockers'] = MainModel.objects.filter(group_id=self.kwargs.get('pk'))
        context['has_perm'] = self.request.user.has_perm('main.change_mainmodel')
        context['all_groups'] = GroupModel.objects.all().count()
        context['all_lockers'] = MainModel.objects.all().count()
        context['all_user_lockers'] = MainModel.objects.filter(user=self.request.user.pk).count()
        context['count_locker_by_username'] = count_locker_by_username
        context['count_locker_by_time'] = count_locker_by_time
        context['count_group_by_time'] = count_group_by_time
        return context

    def get_success_url(self):
        messages.success = "Group was edited successfully!"
        return reverse_lazy('details user', kwargs={'pk': self.request.user.pk})


