from .serializers import PostListSerializer, PostDetailSerializer, \
    CategoryListSerializer
from blog.models import Post, Category
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework import mixins


class PostListAPIView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class PostDetailAPIView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class PostCreateAPIView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    permission_classes = [IsAdminUser]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PostPutDeleteAPIView(mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = [IsAdminUser]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class PostListByCategory(APIView):
    @staticmethod
    def get(request, pk):
        posts = Post.objects.filter(category_id=pk)
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)


class CategoryListAPIView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CategoryDetailAPIView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class CategoryCreateAPIView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    permission_classes = [IsAdminUser]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CategoryPutDeleteAPIView(mixins.UpdateModelMixin,
                               mixins.DestroyModelMixin,
                               generics.GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    permission_classes = [IsAdminUser]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
