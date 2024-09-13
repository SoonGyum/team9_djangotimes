from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import Article
from .serializers import ArticleSerializer


# Create your views here.
class ArticleListView(ListAPIView):
    queryset = Article.objects.all()  # 모든 Article 객체 가져오기
    serializer_class = ArticleSerializer  # 직렬화에 사용할 serializer 지정
