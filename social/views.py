from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Follow, Block
from .serializers import FollowSerializer, BlockSerializer

class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Users can only see who they are following
        return Follow.objects.filter(follower=self.request.user)

    def perform_create(self, serializer):
        # Auto-set the 'follower' to the current user
        serializer.save(follower=self.request.user)

class BlockViewSet(viewsets.ModelViewSet):
    serializer_class = BlockSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Block.objects.filter(blocker=self.request.user)

    def perform_create(self, serializer):
        serializer.save(blocker=self.request.user)