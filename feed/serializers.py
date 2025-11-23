from rest_framework import serializers
from .models import Activity

class ActivitySerializer(serializers.ModelSerializer):
    actor_username = serializers.ReadOnlyField(source='actor.username')
    target_str = serializers.SerializerMethodField()

    class Meta:
        model = Activity
        fields = ['actor_username', 'verb', 'target_str', 'created_at']

    def get_target_str(self, obj):
        return str(obj.target)