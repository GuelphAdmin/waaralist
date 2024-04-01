from django.contrib import admin

# Register your models here.
from .models import memberdetails,waaradata


class TaskAdmin(admin.ModelAdmin):
    list_display = ('firstname','lastname','phonenumber','is_completed')
    search_fields = ('firstname',)

admin.site.register(memberdetails,TaskAdmin)

class waaradataclass(admin.ModelAdmin):
    list_display = ('firstname','lastname','phonenumber','is_completed','created_at','updated_at')
    search_fields = ('firstname',)

admin.site.register(waaradata,waaradataclass)
