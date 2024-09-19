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

from .models import Article, Category, Like
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

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        title = request.data.get("title")
        content = request.data.get("content")
        file = request.data.get("file")
        url = request.data.get("url")
        category_id_text = request.data.get("category")

        category = Category.objects.get(id=category_id_text)

        article = Article.objects.create(
            title=title,
            content=content,
            file=file,
            url=url,
            category=category,
            user = request.user,
        )

        serializer = ArticleSerializer(article)
        return Response(serializer.data)


class CategoryListView(ListAPIView):
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


class LikeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, article=article)
        
        if created:
            return Response({"message": "좋아요가 추가되었습니다."}, status=status.HTTP_201_CREATED)
        else:
            like.delete()
            return Response({"message": "좋아요가 취소되었습니다."}, status=status.HTTP_204_NO_CONTENT)