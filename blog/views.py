from .models import Post, Category, Comment
from blog import forms
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm


class HomeView(generic.ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']


class CategoryView(generic.DetailView):
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


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'post_details.html'


class AddPostView(generic.CreateView):
    model = Post
    form_class = forms.PostForm
    template_name = 'add_post.html'


class AddCategoryView(generic.CreateView):
    model = Category
    form_class = forms.AddCategoryForm
    template_name = 'add_category.html'


class UpdatePostView(generic.UpdateView):
    model = Post
    form_class = forms.EditForm
    template_name = 'update_post.html'


class DeletePostView(generic.DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


class AddCommentView(generic.CreateView):
    model = Comment
    form_class = forms.AddCommentForm
    template_name = 'add_comment.html'

    def get_success_url(self):
        current_post_id = self.kwargs['pk']
        return reverse_lazy('post-detail', kwargs={'pk': current_post_id})

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.author_id = self.request.user.id
        return super().form_valid(form)
