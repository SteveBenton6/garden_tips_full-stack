# Create your views here.
from django.shortcuts import render

# from django.views.generic import TemplateView
from django.views import generic
from .models import GardenTip

"""
class HomePage(TemplateView):

    # Displays home page"

    template_name = 'index.html'
"""

class TipsList(generic.ListView):
    queryset = GardenTip.objects.all()
    template_name = "tips_list.html"