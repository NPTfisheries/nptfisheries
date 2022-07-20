from django.shortcuts import render
from django.views.generic import ListView, CreateView
#from django_tables2 import SingleTableView
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from .models import Document
from .forms import DocumentForm
from .tables import DocumentTable
from .filters import DocumentFilter

# Create your views here.
#class DocumentList(ListView):
#	model = Document
#	template_name = 'document_list.html'
	#ordering = ['-upload_date']

#class DocumentList(SingleTableView):
#	model = Document
#	table_class = DocumentTable
#	template_name = 'document_list.html'

class DocumentList(SingleTableMixin, FilterView):
	model = Document
	table_class = DocumentTable
	template_name = 'document_list.html'
	filterset_class = DocumentFilter

class DocumentUpload(CreateView):
	model = Document
	form_class = DocumentForm
	template_name = 'document_upload.html'