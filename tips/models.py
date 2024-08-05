from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))
SEASON = (("Spring", "SPRING"), ("Summer", "SUMMER"), ("Autumn", "AUTUMN"), ("Winter", "WINTER" ))
REGION = (("Southern England", "SOUTHERN ENGLAND"), ("West of England", "WESTERN ENGLAND"), ("Wales", "WALES"),
    ("North of England", "NORTEHRN ENGLAND"), ("Scotland", "SCOTLAND"), ("Northern Ireland", "NORTHERN IRELAND"),
     ("Midlands", "MIDLANDS"), ("Outside the UK", "NON UK"))
SCORE = ((" ", "Score 0 out of 5"), ("*", "Score 1 out of 5"), ("**", "Score 2 out of 5"), ("***", "Score 3 out of 5"),
     ("****", "Score 4 out of 5"), ("*****", "Score 5 out of 5"))

# Create your models here.

class GardenTip(models.Model):
    """
    Stores a single Tip entry related to the model:"auth.User".

    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "tip_creator")
    season = models.CharField(choices=SEASON, default="summer")
    region = models.CharField(choices=REGION, default="SE")
    image = CloudinaryField('image', default='placeholder')
    garden_tip = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Tip: {self.title} | a tip by {self.creator}"



class Feedback(models.Model):
    """
    Stores a single Feedback entry related to the model:"auth.User" and model:"GardenTip".

    """
    post = models.ForeignKey(GardenTip, on_delete=models.CASCADE, related_name = "feedback")
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "respondent")
    tip_feedback = models.TextField()
    score = models.CharField(choices=SCORE, default=" ")
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Feedback: {self.tip_feedback} | feedback from {self.creator}"