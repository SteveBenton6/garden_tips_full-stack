from django.contrib import admin
from .models import GardenTip, Feedback

# Register your models here.
admin.site.register(GardenTip)
admin.site.register(Feedback)
# Line for each model