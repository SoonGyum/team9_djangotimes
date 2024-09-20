from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path("", views.ArticleListView.as_view(), name="article_list"),
    path("<int:pk>/", views.ArticleDetailView.as_view(), name="article_detail"),
    path("category/", views.CategoryListView.as_view(), name="category_list"),
    path("<int:pk>/like/", views.LikeView.as_view(), name="article_like"),
    path("liked-articles/", views.LikedArticlesView.as_view(), name="liked_articles"),
    path("<int:pk>/comments/", views.CommentListAPIView.as_view(), name="comment_list"),
    path(
        "comments/<int:comment_pk>/",
        views.CommentDetailAPIView.as_view(),
        name="comment_detail",
    ),
    path("comments/<int:comment_pk>/like/", views.CommentLikeView.as_view(), name="comment_like"),
    path("liked-comments/", views.LikedCommentsView.as_view(), name="liked_comments"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
