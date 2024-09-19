from rest_framework import serializers
from .models import Article, Category, Like


class ArticleSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    file = serializers.FileField(required=False)
    user = serializers.StringRelatedField()  # user 필드도 이름이나 관련 필드를 보여줌
    like_count = serializers.IntegerField(source="likes.count", read_only=True)

    class Meta:
        model = Article
        fields = ["id", "title", "content", "category", "user", "file", "url", "like_count"]
        ordering = ["-id"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'user', 'article', 'created_at']