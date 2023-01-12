from PassLocker.groups.models import GroupModel


def get_group():
    return GroupModel.objects.all()
