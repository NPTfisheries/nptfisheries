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

	def get_context_data(self, **kwargs):
		data = super().get_context_data(**kwargs)
		connected_comments = Comment.objects.filter(CommentPost=self.get_object())
		number_of_comments = connected_comments.count()
		data['comments'] = connected_comments
		data['no_of_comments'] = number_of_comments
		data['comment_form'] = CommentForm()
		return data

	def post(self, request, *args, **kwargs):
		if self.request.method == 'POST':
			print('-------------------------------------------------------------------------------Reached here')
			comment_form = CommentForm(self.request.POST)
			if comment_form.is_valid():
				content = comment_form.cleaned_data['content']
				try:
					parent = comment_form.cleaned_data['parent']
				except:
					parent=None
			new_comment = Comment(content=content , author = self.request.user , CommentPost=self.get_object() , parent=parent)
			new_comment.save()
			return redirect(self.request.path_info)			


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