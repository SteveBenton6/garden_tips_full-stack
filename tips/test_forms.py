from django.test import TestCase
from .forms import GardenTipsForm, FeedbackForm

class TestFeedbackForm(TestCase):

    def test_form_is_valid(self):
        feedback_form = FeedbackForm({'tip_feedback': 'This is a great tip', 'score': "Score 2 out of 5"})
        self.assertTrue(feedback_form.is_valid(), msg="Form is invalid")
    
    def test_form_is_invalid(self):
        feedback_form = FeedbackForm({'tip_feedback': '', 'score': ""})
        self.assertFalse(feedback_form.is_valid(), msg="Form is valid")

