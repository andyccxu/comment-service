from django.urls import path
from .views import CommentListCreate

urlpatterns = [
    path('comments/', CommentListCreate.as_view(), name='comment-list-create'),
]
