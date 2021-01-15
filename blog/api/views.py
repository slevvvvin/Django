from blog.api import serializers
from blog.models import Post, Category
from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions


class PostListView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostListSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class PostDetailView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostDetailSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class PostCreateView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostListSerializer
    permission_classes = [permissions.IsAdminUser]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PostUpdateView(mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostDetailSerializer
    permission_classes = [permissions.IsAdminUser]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class PostDeleteView(mixins.DestroyModelMixin,
                     generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostDetailSerializer
    permission_classes = [permissions.IsAdminUser]

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class PostListByCategory(APIView):
    @staticmethod
    def get(request, pk):
        posts = Post.objects.filter(category_id=pk)
        serializer = serializers.PostListSerializer(posts, many=True)
        return Response(serializer.data)


class CategoryListView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategoryListSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CategoryDetailView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategoryListSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class CategoryCreateView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategoryListSerializer
    permission_classes = [permissions.IsAdminUser]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CategoryUpdateView(mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategoryListSerializer
    permission_classes = [permissions.IsAdminUser]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class CategoryDeleteView(mixins.DestroyModelMixin,
                         generics.GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategoryListSerializer
    permission_classes = [permissions.IsAdminUser]

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
