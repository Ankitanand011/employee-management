from django.contrib import admin

# Register your models here.
from .models import Employee, Department

admin.site.register(Department)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "role", "salary", "department")
    search_fields = ("name", "role")
    list_filter = ("role", "department")
    ordering = ("-salary",)