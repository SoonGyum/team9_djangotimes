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

from .models import Article, Category, Like, Comment, CommentLike
from .serializers import ArticleSerializer, CommentSerializer, ArticleDetailSerializer


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
            user=request.user,
        )

        serializer = ArticleSerializer(article)
        return Response(serializer.data)


class CategoryListView(ListAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class ArticleDetailView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        return get_object_or_404(Article, pk=pk)

    def get(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleDetailSerializer(article)
        return Response(serializer.data)

    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleDetailSerializer(article, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        data = {"pk": f"{pk} is deleted."}
        return Response(data, status=status.HTTP_200_OK)


class CommentListAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        comments = article.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        content = request.data.get("content")
        comment = Comment.objects.create(
            article=article,
            content=content,
            user=request.user,
        )
        serializer = CommentSerializer(comment)
        return Response(serializer.data)


class CommentDetailAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, comment_pk):
        return get_object_or_404(Comment, pk=comment_pk)

    def put(self, request, comment_pk):
        comment = self.get_object(comment_pk)
        content = request.data.get("content")

        # 필드 값을 직접 수정
        comment.content = content
        comment.user = request.user
        comment.save()
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def delete(self, request, comment_pk):
        comment = self.get_object(comment_pk)
        comment.delete()
        data = {"pk": f"{comment_pk} is deleted."}
        return Response(data, status=status.HTTP_204_NO_CONTENT)


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


class LikedArticlesView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ArticleSerializer

    def get_queryset(self):
        return Article.objects.filter(likes__user=self.request.user)


class CommentLikeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, comment_pk):
        comment = get_object_or_404(Comment, pk=comment_pk)
        like, created = CommentLike.objects.get_or_create(user=request.user, comment=comment)

        if created:
            return Response({"message": "댓글에 좋아요를 눌렀습니다."}, status=status.HTTP_201_CREATED)
        else:
            like.delete()
            return Response({"message": "댓글에 좋아요를 취소했습니다."}, status=status.HTTP_204_NO_CONTENT)


class LikedCommentsView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(likes__user=self.request.user)
