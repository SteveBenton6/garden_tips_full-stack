from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    """
    Form class for users to give feedback on a post
    """
    class Meta:
        """
        Specify the Django model and order of the fields
        """
        model = Feedback
        fields = ('tip_feedback', 'score',)