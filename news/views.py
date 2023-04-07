from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy

# Create your views here.
#def news_list(request):
#	return render(request, 'news_list.html', {})

class NewsList(ListView):
	model = Post
	template_name = 'news/news_list.html'
	#ordering = ['-id']
	ordering = ['-post_date']

class NewsDetail(DetailView):
	model = Post
	template_name = 'news/news_detail.html'

		


class NewsPost(PermissionRequiredMixin, CreateView):
	model = Post
	form_class = PostForm
	template_name = 'news/news_post.html'
	permission_required = ('news.add_post')
	#fields = '__all__'
	#field = ('title', 'uploaded_by', 'primary_author', 'secondary_authors', 'body')

class NewsEdit(PermissionRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	form_class = PostForm
	template_name = 'news/news_edit.html'
	permission_required = ('news.change_post')
	#fields = '__all__'
	
	def test_func(self):
		obj = self.get_object()
		return obj.uploaded_by.name.user == self.request.user

class NewsDelete(PermissionRequiredMixin, DeleteView):
	model = Post
	template_name = 'news/news_delete.html'
	success_url = reverse_lazy('news_list')
	permission_required = ('news.delete_post')