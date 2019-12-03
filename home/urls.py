from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PostViewSet, UserViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'users', UserViewSet, basename='user')
urlpatterns = router.urls
