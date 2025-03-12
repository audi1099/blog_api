from django.urls import path
from .views import PostViewSet, CommentViewSet

urlpatterns = [
    path('posts/', PostViewSet.as_view({'get': 'list', 'post': 'create'})),  # Список и создание постов
    path('posts/<int:pk>/', PostViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),  # Детали, обновление и удаление поста
    path('comments/', CommentViewSet.as_view({'get': 'list', 'post': 'create'})),  # Список и создание комментариев
    path('comments/<int:pk>/', CommentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),  # Детали, обновление и удаление комментария
]