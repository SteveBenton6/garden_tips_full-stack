from . import views
from django.urls import path

urlpatterns = [
    path('', views.TipsList.as_view(), name='home'),
]