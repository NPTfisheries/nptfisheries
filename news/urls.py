# blog/urls.py
from django.urls import path
from .views import NewsList, NewsDetail, NewsPost, NewsEdit, NewsDelete

urlpatterns = [
	path('', NewsList.as_view(), name = 'news_list'),
	path('<int:pk>/', NewsDetail.as_view(), name='news_detail'),
	path('post/', NewsPost.as_view(), name='news_post'),
    path('edit/<int:pk>/', NewsEdit.as_view(), name='news_edit'),
    path('delete/<int:pk>/', NewsDelete.as_view(), name='news_delete'),
]