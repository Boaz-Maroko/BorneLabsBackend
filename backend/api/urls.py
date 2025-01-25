from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IdeaViewSet, IdeaReviewViewSet, StoryViewSet, MessageViewSet, SavedIdeaViewSet, NotificationViewSet, CommunityRequestViewSet

router = DefaultRouter()
router.register(r'ideas', IdeaViewSet)
router.register(r'idea-reviews', IdeaReviewViewSet)
router.register(r'stories', StoryViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'saved-ideas', SavedIdeaViewSet)
router.register(r'notifications', NotificationViewSet)
router.register(r'community-requests', CommunityRequestViewSet)

urlpatterns = router.urls
