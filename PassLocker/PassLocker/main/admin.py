from django.contrib import admin

from PassLocker.main.models import MainModel


# Register your models here.
@admin.register(MainModel)
class MainAdmin(admin.ModelAdmin):
    list_display = ("software_name", "url", "username", "password", "comment", "created_date", "updated_date", "group", "user")
    list_filter = ("software_name",)
    list_per_page = 10
    search_fields = ("software_name", "username",)