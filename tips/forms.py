from django import forms
from .models import Feedback, GardenTip

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



class GardenTipsForm(forms.ModelForm):
    """
    Form class for users to submit a tip
    """
    class Meta:
        """
        Specify the Django model and order of the fields
        """
        model = GardenTip
        fields = ('season', 'region', 'image', 'garden_tip' )