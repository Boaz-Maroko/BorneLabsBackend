from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer



# views
# Viewsets provide functionality for all RESTful CRUD endpoints

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer