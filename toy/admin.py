from django.contrib import admin

from .models import Toy


class ToyAdmin(admin.ModelAdmin):
    list_display = ['title', 'location']


admin.site.register(Toy, ToyAdmin)
