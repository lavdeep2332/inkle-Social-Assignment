from rest_framework import viewsets, permissions
from .models import Post, Like
from .serializers import PostSerializer, LikeSerializer
from social.models import Block
from .permissions import IsOwnerOrAdmin
from feed.models import Activity

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
    def perform_destroy(self, instance):
        # 1. Create the Activity Log BEFORE deleting
        # We target the 'author' of the post, so the link doesn't break
        Activity.objects.create(
            actor=self.request.user, 
            verb=f"deleted a post by {instance.author.username}",
            target=instance.author 
        )
        instance.delete()
class LikeViewSet(viewsets.ModelViewSet):
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)