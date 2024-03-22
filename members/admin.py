from django.contrib import admin

# Register your models here.
from .models import memberdetails


class TaskAdmin(admin.ModelAdmin):
    list_display = ('firstname','lastname','phonenumber','is_completed')
    search_fields = ('firstname',)

admin.site.register(memberdetails,TaskAdmin)
