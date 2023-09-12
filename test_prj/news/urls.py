from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_news, name="home_news"),
    path('create', views.create, name="create"),
    path('<int:pk>', views.NewsDetailView.as_view(), name="detail_view"),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name="news_delete"),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name="news_update"),
    path('list_view', views.NewsListView.as_view(), name="list_view")
]
