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
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
