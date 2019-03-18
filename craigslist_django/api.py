from rest_framework.routers import DefaultRouter
from craigslist.views import CategoryViewSet, PostViewSet
from rest_framework_extensions.routers import NestedRouterMixin


# router = DefaultRouter()

# router.register('categories', CategoryViewSet)
# router.register('posts', PostViewSet)


class NestedDefaultRouter(NestedRouterMixin, DefaultRouter):
  pass
  

router = NestedDefaultRouter()

categories_router = router.register('categories', CategoryViewSet)
categories_router.register(
    'posts', PostViewSet,
    base_name='category-posts',
    parents_query_lookups=['category'])

router.register(r'posts', PostViewSet, basename='post')  #8000/posts/postID
