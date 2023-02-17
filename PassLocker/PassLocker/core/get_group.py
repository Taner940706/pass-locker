from PassLocker.groups.models import GroupModel


# get all groups
def get_group():
    return GroupModel.objects.all()
