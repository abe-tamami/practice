from django.contrib import admin

# Register your models here.
from .models import Fusen

class FusenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_datetime', 'updated_datetime')
    list_display_links = ('id', 'title')

admin.site.register(Fusen, FusenAdmin)
