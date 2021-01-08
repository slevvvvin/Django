from .serializers import PostListSerializer, PostDetailSerializer, \
    CategoryListSerializer
from blog.models import Post, Category
from rest_framework import generics
from rest_framework.response import Response


class PostListAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer


class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer


class CategoryListAPIView(generics.ListCreateAPIView):

    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer

    @staticmethod
    def get(request, pk):
        posts = Post.objects.filter(category_id=pk)
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)
