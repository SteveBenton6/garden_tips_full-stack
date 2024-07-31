from django.urls import path
from . import views
"""
urlpatterns = [
    path("read/<id>", views.view_tips, name='home'),
]




"""
urlpatterns = [
    path("", views.TipList.as_view(), name='home'),
]

