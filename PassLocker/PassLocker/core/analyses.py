from PassLocker.main.models import MainModel


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
