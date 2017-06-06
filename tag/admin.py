from django.contrib import admin

from .models import Tag


class TagAdmin(admin.ModelAdmin):
    fields = ['display_name']
    list_display = ['display_name', 'code']


admin.site.register(Tag, TagAdmin)
