from django.urls import path
from . import views

urlpatterns = [
    path("", views.TipList.as_view(), name='home'),
    path('createtip/', views.create_tip, name='create_tip'),
    path('edit_detail/<slug:slug>/', views.tips_detail, name='tips_detail'),
    path('edit_tip/<slug:slug>/', views.tip_edit, name='tip_edit'),
    path('delete_tip/<slug:slug>/', views.tip_delete, name='tip_delete'),
    path('<slug:slug>/edit_comment/<int:comment_id>', views.feedback_edit, name='feedback_edit'),
    path('<slug:slug>/delete_feedback/<int:comment_id>', views.feedback_delete, name='feedback_delete'),
    # path('<slug:slug>/tip_edit/<int:post_id>', views.tip_edit, name='tip_edit'),
    # path('<slug:slug>/delete_tip/<int:post_id>', views.tip_delete, name='tip_delete'),
    # path('createtip/', views.create_tip, name='create_tip'),
]

