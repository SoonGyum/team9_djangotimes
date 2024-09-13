from django.db import models
from accounts.models import User


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(models.Model):
    CATEGORY_CHOICES = (
        ("1", "정치"),
        ("2", "경제"),
        ("3", "사회"),
        ("4", "생활/문화"),
        ("5", "세계"),
        ("6", "IT/과학"),
    )
    name = models.CharField(max_length=1, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name


class Article(TimeStampedModel):
    title = models.CharField(max_length=30)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to="articles/", null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # url은 선택사항
    url = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.category, self.title, self.user
