from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path("", views.ArticleListView.as_view(), name="article_list"),
    path("create/", views.ArticleCreateView.as_view(), name="article_create"),
    path("<int:pk>/", views.ArticleDetailView.as_view(), name="article_detail"),
    path("<int:pk>/update/", views.ArticleUpdateView.as_view(), name="article_update"),
    path("<int:pk>/delete/", views.ArticleDeleteView.as_view(), name="article_delete"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
