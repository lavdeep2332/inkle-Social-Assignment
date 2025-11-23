from rest_framework import serializers
from .models import Follow, Block

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ['following'] # We only need to know WHO to follow

class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = ['blocked']