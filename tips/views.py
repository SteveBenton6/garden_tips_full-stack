from django.shortcuts import render, get_object_or_404, reverse

from django.views import generic
from .models import GardenTip

# Create your views here.
"""
class HomePage(TemplateView):

    # Displays home page"

    template_name = 'index.html'
"""

class TipList(generic.ListView):
    queryset = GardenTip.objects.filter(status=1)
    # queryset = GardenTip.objects.filter(status=1) -- To Hide Drafts
    # template_name = "tips/tips_list.html"
    template_name = "tips/index.html"
    paginate_by = 6
    


"""
def show_article(request, tips_id):
    retrieved_tips = get_object_or_404(GardenTip, id=tips_id)
    context - {
        "article": retrieved_tips,
    }

    return render(request, "articles/tips_list.html", context )
"""
def tips_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = GardenTip.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "tips/tips_detail.html",
        {"post": post},
    )

