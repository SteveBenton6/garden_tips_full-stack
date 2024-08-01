from django.shortcuts import render, get_object_or_404

from django.views import generic
from .models import GardenTip

# Create your views here.
"""
class HomePage(TemplateView):

    # Displays home page"

    template_name = 'index.html'
"""

class TipList(generic.ListView):
    queryset = GardenTip.objects.all().order_by("-created_on")
    # queryset = GardenTip.objects.filter(status=1) -- To Hide Drafts
    template_name = "tips/tips_list.html"

    


"""
def show_article(request, tips_id):
    retrieved_tips = get_object_or_404(GardenTip, id=tips_id)
    context - {
        "article": retrieved_tips,
    }

    return render(request, "articles/tips_list.html", context )
"""
