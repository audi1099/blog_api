from django.urls import path
from .views import PostViewSet, CommentViewSet

urlpatterns = [
    path('posts/', PostViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('posts/<int:pk>/', PostViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('comments/', CommentViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('comments/<int:pk>/', CommentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]