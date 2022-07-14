from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy

# Create your views here.
#def news_list(request):
#	return render(request, 'news_list.html', {})

class NewsList(ListView):
	model = Post
	template_name = 'news_list.html'
	#ordering = ['-id']
	ordering = ['-post_date']


class NewsDetail(DetailView):
	model = Post
	template_name = 'news_detail.html'

class NewsPost(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'news_post.html'
	#fields = '__all__'
	#field = ('title', 'uploaded_by', 'primary_author', 'secondary_authors', 'body')

class NewsEdit(UpdateView):
	model = Post
	form_class = PostForm
	template_name = 'news_edit.html'
	#fields = '__all__'

class NewsDelete(DeleteView):
	model = Post
	template_name = 'news_delete.html'
	success_url = reverse_lazy('news_list')