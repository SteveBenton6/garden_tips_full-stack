from django.shortcuts import render, get_object_or_404, reverse

from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import GardenTip, Feedback
from .forms import FeedbackForm

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
        An instance of :model:`tips.`.

    **Template:**

    :template:`tips/tips_detail.html`
    """

    queryset = GardenTip.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.feedback.all().order_by("-created_on")
    comment_count = post.feedback.filter(approved=True).count()

    if request.method == "POST":
        comment_form = FeedbackForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.creator = request.user
            comment.post = post
            comment.save()
            messages.add_message(
            request, messages.SUCCESS,
            'Feedback submitted and awaiting approval'
        )

    comment_form = FeedbackForm()


    return render(
        request,
        "tips/tips_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )


def feedback_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = GardenTip.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Feedback, pk=comment_id)
        comment_form = FeedbackForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.creator == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('tips_detail', args=[slug]))


def feedback_delete(request, slug, comment_id):
    """
    view to delete feedback
    """
    queryset = GardenTip.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Feedback, pk=comment_id)

    if comment.creator == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('tips_detail', args=[slug]))




