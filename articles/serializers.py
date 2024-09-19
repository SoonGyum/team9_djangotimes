from rest_framework import serializers
from .models import Article, Category, Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = [
            "article",
        ]

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret.pop("article")
        return ret


class ArticleSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    file = serializers.FileField(required=False)
    user = serializers.StringRelatedField()

    class Meta:
        model = Article
        fields = ["id", "title", "content", "category", "user", "file", "url"]
        ordering = ["-id"]

    def to_representation(self, instance):
        ret = super().to_representation(instance)

        ret["category"] = CategorySerializer(instance.category).data
        return ret


class ArticleDetailSerializer(ArticleSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    comments_count = serializers.IntegerField(source="comments.count", read_only=True)
