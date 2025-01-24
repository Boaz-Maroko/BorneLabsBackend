from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="settings")
    theme = models.CharField(max_length=20, choices=[('Light', 'Light'), ('Dark', 'Dark')], default='Light')
    notifications_enabled = models.BooleanField(default=True)
    language_preference = models.CharField(max_length=10, default="en")

    def __str__(self):
        return f"Settings for {self.user.username}"
