from django.db import models
from accounts.models import User


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(models.Model):
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


class Article(TimeStampedModel):
    title = models.CharField(max_length=30)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='articles')
    # file은 선택사항
    file = models.FileField(upload_to="articles/", null=True, blank=True)
    category = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
        related_name="articles",
    )
    # url은 선택사항
    url = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey('Article', on_delete=models.CASCADE, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'article')


class Comment(TimeStampedModel):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="comments"
    )
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class CommentLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey('Comment', on_delete=models.CASCADE, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'comment')