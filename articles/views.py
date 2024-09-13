from django.db.models import Q
from rest_framework import status
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.generics import (
    ListCreateAPIView,
    get_object_or_404,
    ListAPIView,
)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

from .models import Article, Category
from .serializers import ArticleSerializer


# Create your views here.
class ArticleListView(ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = PageNumberPagination
    serializer_class = ArticleSerializer

    def get_queryset(self):
        search = self.request.query_params.get("search")
        if search:
            return Article.objects.filter(
                Q(title__icontains=search) | Q(content__icontains=search)
            )
        return Article.objects.all()

    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)

    def post(self, request):
        title = request.get("title")
        content = request.get("content")
        file = request.get("file")
        url = request.get("url")
        category_id_text = request.get("category")

        category = Category.objects.get(id=category_id_text)

        article = Article.objects.create(
            title=title,
            content=content,
            file=file,
            url=url,
            category=category,
        )

        serializer = ArticleSerializer(article)
        return Response(serializer.data)


class CategoryListView(APIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class ArticleDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        return get_object_or_404(Article, pk=pk)

    def get(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        data = {"pk": f"{pk} is deleted."}
        return Response(data, status=status.HTTP_200_OK)
