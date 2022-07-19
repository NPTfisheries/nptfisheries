from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Document
from .forms import DocumentForm

# Create your views here.
class DocumentList(ListView):
	model = Document
	template_name = 'document_list.html'
	#ordering = ['-upload_date']

class DocumentUpload(CreateView):
	model = Document
	form_class = DocumentForm
	template_name = 'document_upload.html'