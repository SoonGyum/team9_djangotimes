from rest_framework import serializers
from .models import Article, Category, Like, Comment, CommentLike
from accounts.models import User


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


class CommentSerializer(serializers.ModelSerializer):
    like_count = serializers.IntegerField(source="likes.count", read_only=True)
    
    class Meta:
        model = Comment
        fields = ["id", "content", "user", "like_count", "created_at", "updated_at"]
        read_only_fields = ["article"]

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret["user"] = instance.user.username
        return ret


class ArticleDetailSerializer(ArticleSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    comments_count = serializers.IntegerField(source="comments.count", read_only=True)

    class Meta:
        model = Article
        fields = [
            "id",
            "title",
            "content",
            "category",
            "user",
            "file",
            "url",
            "like_count",
            "comments_count",
            "comments",
        ]
        ordering = ["-id"]