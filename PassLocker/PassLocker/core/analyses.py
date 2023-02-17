from PassLocker.groups.models import GroupModel
from PassLocker.main.models import MainModel


# diagram for count of lockers by username
def count_locker_by_username():
    label_username = []
    data_username = []
    lockers = MainModel.objects.all()
    for locker in lockers:
        if locker.username not in label_username:
            label_username.append(locker.username)
    for lab in label_username:
        data_username.append(MainModel.objects.filter(username=lab).count())
    context = {
        'label_username': label_username,
        'data_username': data_username,
    }
    return context


# diagram for count of lockers in time
def count_locker_by_time():
    label_in_time = []
    data_in_time = []
    lockers = MainModel.objects.all().order_by('created_date')
    for locker in lockers:
        if locker.created_date not in label_in_time:
            label_in_time.append(locker.created_date)
    for lab in label_in_time:
        data_in_time.append(MainModel.objects.filter(created_date=lab).count())
    context = {
        'label_in_time': label_in_time,
        'data_in_time': data_in_time,
    }
    return context


# diagram for count of groups in time
def count_group_by_time():
    label_group_in_time = []
    data_group_in_time = []
    groups = GroupModel.objects.all().order_by('created_date')
    for group in groups:
        if group.created_date not in label_group_in_time:
            label_group_in_time.append(group.created_date)
    for lab in label_group_in_time:
        data_group_in_time.append(GroupModel.objects.filter(created_date=lab).count())
    context = {
        'label_group_in_time': label_group_in_time,
        'data_group_in_time': data_group_in_time,
    }
    return context
