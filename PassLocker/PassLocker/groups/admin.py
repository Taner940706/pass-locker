from django.contrib import admin

from PassLocker.groups.models import GroupModel


# Register your models here.
@admin.register(GroupModel)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("group_name", "description", "created_date", "updated_date",)
    list_per_page = 10
    list_filter = ("group_name",)
    search_fields = ("group_name__contains",)