from django.urls import path, include 
from .views import CategoryViewSet, PostViewSet # This library gives us all of the functions usually found in views.py
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'', CategoryViewSet, basename='category')
# urlpatterns = router.urls


from rest_framework_extensions.routers import ExtendedSimpleRouter
router = ExtendedSimpleRouter()
(
    router.register(r'categories', CategoryViewSet, base_name='category')
        .register(r'posts',
                    PostViewSet,
                    base_name='categories-post',
                    parents_query_lookups=['posts'])
)
router.register(r'posts', PostViewSet, basename='post')
# router.register(r'posts', PostViewSet, basename='post')

urlpatterns = router.urls
