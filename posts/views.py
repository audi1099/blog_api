from rest_framework import viewsets, filters
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .filters import PostFilter
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_class = PostFilter
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["id", "title", "content", "author", "created_at"]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name="ordering",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description="Сортировка по полям: id, title, content, author, created_at. Пример: ?ordering=-created_at",
            ),
        ],
        operation_description="Получить список постов с сортировкой"
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

