# doc_lib/urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.DocumentList.as_view(), name = 'document_list'),
    #path('upload', views.DocumentUpload.as_view(), name = 'document_upload'),
    path('upload', views.DocumentUpload, name = 'document_upload'),
]