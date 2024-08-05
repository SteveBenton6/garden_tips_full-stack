from django.urls import path
from . import views
"""
urlpatterns = [
    path("read/<id>", views.view_tips, name='home'),
]




"""
urlpatterns = [
    path("", views.TipList.as_view(), name='home'),
    path('<slug:slug>/', views.tips_detail, name='tips_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>', views.feedback_edit, name='feedback_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>', views.feedback_delete, name='feedback_delete'),
    
]

