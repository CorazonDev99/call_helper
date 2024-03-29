from django.contrib import admin

from breaks.models import organisations, groups


@admin.register(organisations.Organisation)
class OrganisationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'director']


@admin.register(groups.Group)
class OrganisationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'manager', 'min_active']


