from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
#from django_tables2 import SingleTableView
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from django.contrib.auth.decorators import permission_required
from .models import Document
from dfrm_admin.models import Employee
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
	template_name = 'documents/document_list.html'
	filterset_class = DocumentFilter

# class DocumentUpload(CreateView):
# 	model = Document
# 	form_class = DocumentForm
# 	template_name = 'document_upload.html'

@permission_required('documents.add_document', raise_exception=True)
def DocumentUpload(request):
	if request.method == 'POST':
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			doc = form.save(commit=False)
			#doc.uploaded_by = request.employee.name
			doc.save()
			form.save_m2m()
			return redirect('document_list')
	else:
		form = DocumentForm()
	return render(request, 'documents/document_upload.html', {'form': form, })