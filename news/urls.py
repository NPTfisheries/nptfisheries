# blog/urls.py
from django.urls import path
from .views import NewsList, NewsDetail, NewsPost, NewsEdit, NewsDelete

urlpatterns = [
	path('', NewsList.as_view(), name = 'news_list'),
	path('<int:pk>', NewsDetail.as_view(), name='news_detail'),
	path('post/', NewsPost.as_view(), name='news_post'),
    #path('post/', NewsPost, name='news_post'),
    path('edit/<int:pk>', NewsEdit.as_view(), name='news_edit'),
    path('<int:pk>/news_delete', NewsDelete.as_view(), name='news_delete'),
  #  path('', views.news_list, name='news_list'),
  #  path('news/<int:pk>/', views.news_detail, name='news_detail'),
  #  path('news/new/', views.news_detail, name='news_new'),
  #  path('news/<int:pk>/edit/', views.news_edit, name='news_edit'),
]