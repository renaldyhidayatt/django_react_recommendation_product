from django.contrib import admin
from .models import Review
from import_export.admin import ImportExportModelAdmin


@admin.register(Review)
class ReviewAdmin(ImportExportModelAdmin):
    list_display = (
        "name",
        "comment",
        "rating",
        "user",
        "sentiment",
        "product",
        "created_at",
        "updated_at",
    )
