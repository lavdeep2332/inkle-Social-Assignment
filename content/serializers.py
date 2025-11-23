from rest_framework import serializers
from .models import Post, Like

class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source='author.username')
    
    class Meta:
        model = Post
        fields = ['id', 'author_username', 'text', 'created_at']
        read_only_fields = ['author']

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['post']