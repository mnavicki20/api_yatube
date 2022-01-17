from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter
from django.urls import include, path
from api.views import CommentViewSet, PostViewSet
from api.views import api_groups, api_groups_detail


router = SimpleRouter()
router.register('posts', PostViewSet)
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('api/v1/api-token-auth/', views.obtain_auth_token),
    path('api/v1/', include(router.urls)),
    path('api/v1/groups/', api_groups),
    path('api/v1/groups/<int:pk>/', api_groups_detail),
]
