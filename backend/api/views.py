from rest_framework import viewsets
from .models import Idea, IdeaReview, Story, Message, SavedIdea, Notification, CommunityRequest
from .serializers import IdeaSerializer, IdeaReviewSerializer, StorySerializer, MessageSerializer, SavedIdeaSerializer, NotificationSerializer, CommunityRequestSerializer

# Idea ViewSet
class IdeaViewSet(viewsets.ModelViewSet):
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer

# IdeaReview ViewSet
class IdeaReviewViewSet(viewsets.ModelViewSet):
    queryset = IdeaReview.objects.all()
    serializer_class = IdeaReviewSerializer

# Story ViewSet
class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializer

# Message ViewSet
class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

# SavedIdea ViewSet
class SavedIdeaViewSet(viewsets.ModelViewSet):
    queryset = SavedIdea.objects.all()
    serializer_class = SavedIdeaSerializer

# Notification ViewSet
class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

# CommunityRequest ViewSet
class CommunityRequestViewSet(viewsets.ModelViewSet):
    queryset = CommunityRequest.objects.all()
    serializer_class = CommunityRequestSerializer
