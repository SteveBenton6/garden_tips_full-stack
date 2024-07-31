from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))
SEASON = (("spring", "SPRING"), ("summer", "SUMMER"), ("autumn", "AUTUMN"), ("winter", "WINTER" ))
REGION = (("SE", "SOUTHERN ENGLAND"), ("WE", "WESTERN ENGLAND"), ("WA", "WALES"),
    ("NE", "NORTEHRN ENGLAND"), ("SC", "SCOTLAND"), ("NI", "NORTHERN IRELAND"), ("MI", "MIDLANDS"))
SCORE = ((1, "*"), (2, "**"), (3, "***"), (4, "****"), (5, "*****"))

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
    garden_tip = models.ForeignKey(GardenTip, on_delete=models.CASCADE, related_name = "feedback")
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "respondent")
    tip_feedback = models.TextField()
    score = models.IntegerField(choices=SCORE, default=3)
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Feedback: {self.tip_feedback} | feedback from {self.creator}"