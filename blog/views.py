from django.views.generic import ListView, DetailView, \
   CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import PostForm, EditForm, AddCategoryForm, AddCommentForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']


class CategoryView(DetailView):
    model = Post
    template_name = 'categories.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryView, self).get_context_data()
        context["category_posts"] = Post.objects.filter(
            category=self.kwargs.get('pk'))
        return context


class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_details.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'


class AddCategoryView(CreateView):
    model = Category
    form_class = AddCategoryForm
    template_name = 'add_category.html'


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


class AddCommentView(CreateView):
    model = Comment
    form_class = AddCommentForm
    template_name = 'add_comment.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.author_id = self.request.user.id
        return super().form_valid(form)
