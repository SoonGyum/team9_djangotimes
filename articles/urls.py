from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path("", views.ArticleListView.as_view(), name="article_list"),
    path("<int:pk>/", views.ArticleDetailView.as_view(), name="article_detail"),
    path("category/", views.CategoryListView.as_view(), name="category_list"),
    path("<int:pk>/comments/", views.CommentListAPIView.as_view(), name="comment_list"),
    path(
        "comments/<int:comment_pk>/",
        views.CommentDetailAPIView.as_view(),
        name="comment_detail",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
