from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from .models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from content.permissions import IsOwnerOrAdmin 
from .models import User
from .serializers import UserSerializer
from feed.models import Activity

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin] # Only Admin/Owner can delete

    def perform_destroy(self, instance):
        # Log the "User deleted by Owner" activity
        Activity.objects.create(
            actor=self.request.user,
            verb=f"deleted user '{instance.username}'",
            target=self.request.user 
        )
        instance.delete()