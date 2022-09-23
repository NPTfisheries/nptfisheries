#doc_lib/tables.py
import django_tables2 as tables
from django_tables2 import A
from django.utils.html import format_html
from .models import Document

class TruncatedTextColumn(tables.Column):
    '''A Column to limit to 100 characters and add an ellipsis'''
    def render(self, value):
        if len(value) > 102:
            return value[0:99] + '...'
        return str(value)


""" class DivWrappedColumn(tables.Column):

    def __init__(self, classname=None, *args, **kwargs):
        self.classname=classname
        super(DivWrappedColumn, self).__init__(*args, **kwargs)

    def render(self, value):
        return mark_safe("<div class='" + self.classname + "' >" +value+"</div>") """

class DocumentTable(tables.Table):

	file = tables.Column()
	def render_file(self, value):
		return format_html('<a href="/media/{}" class="btn btn-primary"><i class="bi bi-download"></i></a>', value)	

	title1 = TruncatedTextColumn(accessor=A('title'))
	#title2 = DivWrappedColumn(classname='title')
	primary_author = tables.Column(verbose_name= 'Author')
	secondary_authors = tables.Column(verbose_name= 'Secondary Authors')
	document_type = tables.Column(verbose_name= 'Type')
	publish_date = tables.Column(verbose_name= 'Published')

	class Meta:
		model = Document
		#attrs = {"class": "paleblue"}
		per_page = 5
		template_name = 'django_tables2/bootstrap.html'
		fields = ('title1', 'primary_author', 'secondary_authors', 'document_type', 'publish_date','file')
		#exclude = ('id', 'uploaded_by', 'upload_date', 'title')