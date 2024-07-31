from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))
SEASON = (("spring", "SPRING"), ("summer", "SUMMER"), ("autumn", "AUTUMN"), ("winter", "WINTER" ))
REGION = (("SE", "SOUTHERN ENGLAND"), ("WE", "WESTERN ENGLAND"), ("WA", "WALES"),
    ("NE", "NORTEHRN ENGLAND"), ("SC", "SCOTLAND"), ("NI", "NORTHERN IRELAND"))

# Create your models here.

class GardenTip(models.Model):
    """
    Stores a single Tip entry related to the model:"auth.User".

    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "tip_creator")
    season = models.IntegerField(choices=SEASON, default=0)
    region = models.IntegerField(choices=REGION, default=0)
    image = CloudinaryField('image', default='placeholder')
    garden_tip = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)