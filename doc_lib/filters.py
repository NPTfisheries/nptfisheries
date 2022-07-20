#doc_lib/filters.py
import django_filters as filters
from .models import Document

class DocumentFilter(filters.FilterSet):
    class Meta:
        model = Document
        fields = {
            'title': ['icontains'],
            'primary_author': ['icontains'],
            'secondary_authors': ['icontains'],
            'publish_date': ['lt', 'gt'],
            'document_type': ['icontains'],
            'keywords': ['icontains'],
        }