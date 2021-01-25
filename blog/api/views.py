from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from blog.api import serializers
from blog.models import Post, Category
from blog.api import permission


class PostView(viewsets.ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permission.IsAdminUserOrReadOnly]


class PostListByCategory(APIView):

    @staticmethod
    def get(request, pk):
        posts = Post.objects.filter(category_id=pk)
        serializer = serializers.PostSerializer(posts, many=True)
        return Response(serializer.data)


class CategoryView(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [permission.IsAdminUserOrReadOnly]
