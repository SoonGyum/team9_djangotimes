from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView, DestroyAPIView,
)
from rest_framework.response import Response
from .models import Article
from .serializers import ArticleSerializer


# Create your views here.
class ArticleListView(ListAPIView):
    permission_classes = [AllowAny]

    queryset = Article.objects.all()  # 모든 Article 객체 가져오기
    serializer_class = ArticleSerializer  # 직렬화에 사용할 serializer 지정


class ArticleCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer = ArticleSerializer(data=request.data)
            serializer.save(user=request.user)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetailView(RetrieveAPIView):
    permission_classes = [AllowAny]

    queryset = Article.objects.all()  # 이 쿼리셋에서 객체를 찾고 업데이트
    serializer_class = ArticleSerializer


class ArticleUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Article.objects.all()  # 이 쿼리셋에서 객체를 찾고 업데이트
    serializer_class = ArticleSerializer

class ArticleDeleteView(DestroyAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
