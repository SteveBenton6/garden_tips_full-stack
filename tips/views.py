from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import GardenTip, Feedback
from .forms import FeedbackForm, GardenTipsForm
from django.contrib.auth.decorators import login_required

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

@login_required
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
            messages.success(request, 'Updated Feedback Submitted for Approval!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating feedback!')

    return HttpResponseRedirect(reverse('tips_detail', args=[slug]))

@login_required
def feedback_delete(request, slug, comment_id):
    """
    Display to delete feedback item
    """
    queryset = GardenTip.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Feedback, pk=comment_id)

    if comment.creator == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Feedback deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own feedback!')

    return HttpResponseRedirect(reverse('tips_detail', args=[slug]))

@login_required
def create_tip(request):
    """
    Display to create a Garden Tip
    """
    if request.method == "POST":
        tip_form = GardenTipsForm(request.POST)
        if tip_form.is_valid():
            tip = tip_form.save(commit=False)
            tip.creator = request.user
            tip.approved = False
            tip_form.save()
            messages.success(request, "Your Garden Tip was Submitted for approval.")
            return redirect("home") 
    else:
        tip_form = GardenTipsForm()
        context = { "tip_form": tip_form,}
        return render(request, "tips/create_tip.html", context)

    
@login_required
def tip_edit(request, slug):
    """
    Display to edit Garden Tip
    """
    queryset = GardenTip.objects.filter(status=1)
    retrieved_tip = get_object_or_404(queryset, slug=slug)

    if not request.user == retrieved_tip.creator:
        messages.error(request, "You cannot edit an article you did not create!")
        return redirect("home") 

    if request.method == "POST":
        tip_form = GardenTipsForm(request.POST, instance=retrieved_tip)
        if tip_form.is_valid():
            tip = tip_form.save(commit=False)
            tip.status = 0
            tip_form.save()
            messages.success(request, "Your edited Garden Tip was Submitted for approval.")
            return redirect("home") 
    else:
        tip_form = GardenTipsForm(instance=retrieved_tip)
        context = {
            "tip_form": tip_form,
            "retrieved_tip": retrieved_tip,
        }
        return render(request, "tips/edit_tip.html", context)

@login_required
def tip_delete(request, slug):
    """
    Display to delete Garden Tip
    """
    queryset = GardenTip.objects.filter(status=1)
    retrieved_tip = get_object_or_404(queryset, slug=slug)

    if not request.user == retrieved_tip.creator:
        messages.error(request, "You cannot delete a Tip you did not create!")
        return redirect("home") 

    if request.method == "POST":
        retrieved_tip.delete()
        messages.success(request, "Your Garden Tip was Deleted.")
        return redirect("home")

    else:
        context = {
            "tip": retrieved_tip,
            "retrieved_tip": retrieved_tip,
        }
        return render(request, "tips/delete_tip.html", context)