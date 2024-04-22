from django.contrib import admin
from django.contrib.admin import StackedInline
from django.db.models import Count
from django.urls import reverse
from django.utils.html import format_html

from breaks.models import replacements, dicts, breaks


#############################
# INLINES
#############################
class ReplacementEmployeeInline(StackedInline):
    model = replacements.ReplacementEmployee



#############################
# MODELS
#############################
@admin.register(replacements.Replacement)
class ReplacementAdmin(admin.ModelAdmin):
    list_display = ('id', 'group', 'date', 'break_start', 'break_end', 'break_max_duration',)
    inlines = (ReplacementEmployeeInline,)


@admin.register(dicts.ReplacementStatus)
class ReplacementAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'sort', 'is_active', )

@admin.register(dicts.BreakStatus)
class BreakStatusAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'sort', 'is_active', )


@admin.register(breaks.Break)
class BreakAdmin(admin.ModelAdmin):
    list_display = ('id', 'replacement_link', 'break_start', 'break_end', '__str__')
    list_filter = ('status__name',)
    empty_value_display = 'unknown'
    radio_fields = {'status': admin.VERTICAL}
    def replacement_link(self, obj):
        link = reverse('admin:breaks_replacement_change', args=[obj.replacement.id])
        return format_html('<a href="{}">{}</a>', link, obj.replacement)









