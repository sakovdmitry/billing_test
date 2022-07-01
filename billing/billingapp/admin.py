from django.contrib import admin

from .models import Client, Organization, Bills


class BillsAdmin(admin.ModelAdmin):
    list_display = (
        'client_name',
        'client_org',
        'sum',
        'date'
        )
    empty_value_display = '-пусто-'


admin.site.register(Bills, BillsAdmin)
admin.site.register(Client)
admin.site.register(Organization)
