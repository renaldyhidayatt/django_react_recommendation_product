from django.contrib import admin
from .models import User
from import_export.admin import ImportExportModelAdmin


@admin.register(User)
class UserAdmin(ImportExportModelAdmin):
    list_display = ("name", "email")
