from rest_framework.routers import DefaultRouter
from .views import UserViewSet


# routes
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = router.urls
