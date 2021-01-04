from rest_framework import serializers
from blog.models import Post, Category, Comment


class PostListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ("title", "id", "category", "body")


class PostDetailSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Post
        fields = '__all__'


class CategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ("id", "name")


class CategoryDetailSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Category
        fields = '__all__'
