from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Import Views
from accounts.views import RegisterView
from content.views import PostViewSet, LikeViewSet
from social.views import FollowViewSet, BlockViewSet
from feed.views import FeedView

# Router Registration
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'likes', LikeViewSet, basename='like')
router.register(r'follows', FollowViewSet, basename='follow')
router.register(r'blocks', BlockViewSet, basename='block')

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Auth
    path('api/register/', RegisterView.as_view(), name='auth_register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # App Logic
    path('api/', include(router.urls)),
    path('api/feed/', FeedView.as_view(), name='feed'),
]