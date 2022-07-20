#doc_lib/tables.py
import django_tables2 as tables
from .models import Document

class DocumentTable(tables.Table):
	class Meta:
		model = Document
		#attrs = {"class": "paleblue"}
		#per_page = 2
		template_name = 'django_tables2/bootstrap.html'
		exclude = ('id', 'uploaded_by', 'upload_date',)