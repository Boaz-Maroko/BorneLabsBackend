from rest_framework import serializers
from .models import Idea, IdeaReview, Story, Message, SavedIdea, Notification, CommunityRequest

# Idea Serializer
class IdeaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idea
        fields = ['id', 'title', 'content', 'tier', 'images', 'approval_count', 'author', 'created_at', 'updated_at']

# IdeaReview Serializer
class IdeaReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdeaReview
        fields = ['id', 'idea', 'reviewer', 'comments', 'rating', 'approval_status', 'created_at']

# Story Serializer
class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ['id', 'author', 'images', 'caption', 'created_at']

# Message Serializer
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'sender', 'receiver', 'content', 'timestamp', 'read']

# SavedIdea Serializer
class SavedIdeaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedIdea
        fields = ['id', 'user', 'idea', 'timestamp']

# Notification Serializer
class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'user', 'message', 'timestamp', 'read']

# CommunityRequest Serializer
class CommunityRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunityRequest
        fields = ['id', 'user', 'message', 'timestamp', 'status']
