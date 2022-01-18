from rest_framework.authtoken import views
from django.urls import path
from api.views import (api_groups, api_groups_detail,
                       api_comments, api_comments_detail,
                       api_posts, api_posts_detail)


urlpatterns = [
    path('api/v1/api-token-auth/', views.obtain_auth_token),
    path('api/v1/posts/', api_posts),
    path('api/v1/posts/<int:pk>/', api_posts_detail),
    path('api/v1/groups/', api_groups),
    path('api/v1/groups/<int:pk>/', api_groups_detail),
    path('api/v1/posts/<int:pk>/comments/', api_comments),
    path('api/v1/posts/<int:post_id>/comments/<int:pk>/', api_comments_detail),
]
