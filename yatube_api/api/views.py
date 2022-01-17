from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework import viewsets

from posts.models import Group, Post
from .permissions import IsAuthorOrReadOnly
from .serializers import CommentSerializer, GroupSerializer, PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    """Вьюсет для публикаций."""
    permission_classes = (IsAuthorOrReadOnly, IsAuthenticated)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


@api_view(['GET'])
def api_groups(request):
    group = Group.objects.all()
    serializer = GroupSerializer(group, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def api_groups_detail(request, pk):
    group = Group.objects.get(id=pk)
    if request.method == 'GET':
        serializer = GroupSerializer(group)
        return Response(serializer.data)
    elif request.method == 'PUT' or request.method == 'PATCH':
        serializer = GroupSerializer(group, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        group.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentViewSet(viewsets.ModelViewSet):
    """Вьюсет для комментариев."""
    permission_classes = (IsAuthorOrReadOnly, IsAuthenticated)
    serializer_class = CommentSerializer

    def get_queryset(self):
        post = Post.objects.get(id=self.kwargs['post_id'])
        return post.comments

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
