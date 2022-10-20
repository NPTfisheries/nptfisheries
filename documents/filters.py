#doc_lib/filters.py
import django_filters as filters
from .models import Document

class DocumentFilter(filters.FilterSet):

# changing the label name as below does not work
    class Meta:
        model = Document
        fields = {
            'title': ['icontains'],
            'publish_date': ['lt', 'gt'],
            'document_type': ['icontains'],
            'keywords': ['icontains'],
            'citation': ['icontains'],
        }