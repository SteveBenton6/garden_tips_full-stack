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


@admin.register(Feedback)
class FeedbackAdmin(SummernoteModelAdmin):
    """
    Lists fields for display in admin, fields for search,
    field filters, fields to prepopulate and rich-text editor.
    """

    list_display = ('tip_feedback', 'approved', 'score', 'creator', 'post')
    search_fields = ['score', 'tip_feedback']
    list_filter = ('approved', 'created_on',)
    summernote_fields = ('tip_feedback',)

# admin.site.register(GardenTip) -- replaced by Summernote
# admin.site.register(Feedback) -- replaced by Summernote
