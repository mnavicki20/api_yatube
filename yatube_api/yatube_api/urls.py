from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from api.views import CommentViewSet, GroupViewSet, PostViewSet

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register('posts/<int:post_id>/comments/', CommentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/api-token-auth/', views.obtain_auth_token),
    path('api/v1/', include(router.urls), name='api-root')
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
