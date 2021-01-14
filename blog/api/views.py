from .serializers import PostListSerializer, PostDetailSerializer, \
    CategoryListSerializer
from blog.models import Post, Category
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class PostListAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    permission_classes = [IsAdminUser]


class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer


class PostListByCategory(APIView):
    @staticmethod
    def get(request, pk):
        posts = Post.objects.filter(category_id=pk)
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)


class CategoryListAPIView(generics.ListCreateAPIView):

    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
