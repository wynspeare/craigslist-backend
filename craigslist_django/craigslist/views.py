from .models import Category, Post
from .serializers import CategorySerializer, PostSerializer
from rest_framework import viewsets
from rest_framework_extensions.mixins import NestedViewSetMixin

class CategoryViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class PostViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()