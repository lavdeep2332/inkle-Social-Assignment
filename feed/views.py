from rest_framework import generics, permissions
from .models import Activity
from .serializers import ActivitySerializer

class FeedView(generics.ListAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticated]