from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PostListSerializer, PostDetailSerializer, \
    CategoryListSerializer, CategoryDetailSerializer
from blog.models import Post, Category, Comment


class PostListAPIView(APIView):
    @staticmethod
    def get(request):
        posts = Post.objects.all()
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)


class PostDetailAPIView(APIView):
    @staticmethod
    def get(request, pk):
        post = Post.objects.get(id=pk)
        serializer = PostDetailSerializer(post)
        return Response(serializer.data)


class CategoryListAPIView(APIView):
    @staticmethod
    def get(request):
        categories = Category.objects.all()
        serializer = CategoryListSerializer(categories, many=True)
        return Response(serializer.data)


class CategoryDetailAPIView(APIView):
    @staticmethod
    def get(request, pk):
        posts = Post.objects.filter(category_id=pk)
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)
