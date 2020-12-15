from django.views.generic import ListView, DetailView, \
   CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']

# TODO: move outside
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data()
        context["cat_menu"] = cat_menu
        return context


class CategoryView(DetailView):
    model = Post
    template_name = 'categories.html'

    def get_context_data(self, *args, **kwargs):
        category_posts = Post.objects.filter(category=self.kwargs.get('pk'))
        context = super(CategoryView, self).get_context_data()
        context["category_posts"] = category_posts
        return context


class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(UserRegisterView, self).get_context_data()
        context["cat_menu"] = cat_menu
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostDetailView, self).get_context_data()
        context["cat_menu"] = cat_menu
        return context


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddPostView, self).get_context_data()
        context["cat_menu"] = cat_menu
        return context


class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddCategoryView, self).get_context_data()
        context["cat_menu"] = cat_menu
        return context


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(UpdatePostView, self).get_context_data()
        context["cat_menu"] = cat_menu
        return context


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(DeletePostView, self).get_context_data()
        context["cat_menu"] = cat_menu
        return context
