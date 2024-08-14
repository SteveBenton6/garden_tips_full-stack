from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import GardenTip, Feedback
from .forms import FeedbackForm, GardenTipsForm

class TipList(generic.ListView):
    """
    Display all Garden Tips
    """
    queryset = GardenTip.objects.filter(status=1)
    template_name = "tips/index.html"
    paginate_by = 6
    
def tips_detail(request, slug):
    """
    Display an individual Garden Tip.

    **Context**
    ``post``
        An instance of :model:`tips.`.
    ``comments``
        All approved comments related to the tip.
    ``comment_count``
        A count of approved feedback related to the post.
    ``comment_form``
        An instance of :form:`blog.CommentForm`
    
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
    Display to edit feedback item
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
    Display to delete feedback
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

def create_tip(request):
    """
    Display to create a tip
    """
    if request.method == "POST":
        tip_form = GardenTipsForm(request.POST, request.FILES)
        if tip_form.is_valid():
            tip = tip_form.save(commit=False)
            tip.creator = request.user
            tip_form.save()
            messages.success(request, "Your Garden Tip was Submitted.")
            return redirect("home") 
    else:
        tip_form = GardenTipsForm()
        context = { "tip_form": tip_form,}
        return render(request, "tips/create_tip.html", context)

    
def tip_edit(request, slug, post_id):
    """
    Display to edit Garden Tip
    """
    if request.method == "POST":

        queryset = GardenTip.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        tip_form = GardenTipsForm(data=request.POST, instance=post)

        if tip_form.is_valid() and post.creator == request.user:
            post = tip_form.save(commit=False)
            post.post = post
            post.approved = False
            post.save()
            messages.add_message(request, messages.SUCCESS, 'Garden Tip Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating Garden Tip!')

    return HttpResponseRedirect(reverse('tips_detail', args=[slug]))


def tip_delete(request, slug, post_id):
    """
    Display to delete Garden Tip
    """
    queryset = GardenTip.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    if post.creator == request.user:
        post.delete()
        messages.add_message(request, messages.SUCCESS, 'Garden Tip deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('tips_detail', args=[slug]))
    
    
