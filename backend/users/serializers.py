from rest_framework import serializers
from .models import UserSettings
from django.contrib.auth.models import User 


# Create serializers
class UserSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSettings
        fields = ['theme', 'notifications_enabled', 'language_preference']

class UserSerializer(serializers.ModelSerializer):
    settings = UserSettingsSerializer()

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'settings']

    def create(self, validated_data):
        # extract nested data
        settings_data = validated_data.pop('settings', None)

        # create the user
        user = User.objects.create_user(**validated_data)
        if settings_data:
            UserSettings.objects.create(user=user, **settings_data)

        return user

    def update(self, instance, validated_data):
        settings_data = validated_data.pop('settings', None)
        if settings_data:
            for attr, value in settings_data.items():
                setattr(instance.settings, attr, value)
            instance.settings.save()
        
        return super().update(instance, validated_data)