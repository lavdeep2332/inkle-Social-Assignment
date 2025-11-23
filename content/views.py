from rest_framework import viewsets, permissions
from .models import Post, Like
from .serializers import PostSerializer, LikeSerializer
from social.models import Block
from .permissions import IsOwnerOrAdmin

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        user = self.request.user
        # Logic: Exclude posts from people who blocked me, or I blocked
        blocked_users = Block.objects.filter(blocker=user).values_list('blocked', flat=True)
        blockers = Block.objects.filter(blocked=user).values_list('blocker', flat=True)
        
        return Post.objects.exclude(author__in=blocked_users).exclude(author__in=blockers)

class LikeViewSet(viewsets.ModelViewSet):
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)