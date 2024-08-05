from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import GardenTip, Feedback

@admin.register(GardenTip) 
class TipAdmin(SummernoteModelAdmin):
    """
    Lists fields for display in admin, fields for search,
    field filters, fields to prepopulate and rich-text editor.
    """

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('garden_tip',)


# Register your models here.
# admin.site.register(GardenTip) -- replaced by Summernote
admin.site.register(Feedback)
# Line for each model