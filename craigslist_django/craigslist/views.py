from .models import Category, Post
from .serializers import CategorySerializer, PostSerializer
from rest_framework import viewsets
from rest_framework_extensions.mixins import NestedViewSetMixin

class CategoryViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PostViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer