from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from myDjangoBlog import settings


class Category(models.Model):
    name = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

    def save(self, *args, **kwargs):
        superuser_id = User.objects.filter(is_superuser=True).values('id')
        self.author_id = superuser_id
        return super(Category, self).save(*args, **kwargs)


class Post(models.Model):
    title = models.CharField(max_length=250)
    title_tag = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')

    def save(self, *args, **kwargs):
        superuser_id = User.objects.filter(is_superuser=True,
                                           username=settings.SUPERUSER_NAME
                                           ).values('id')
        self.author_id = superuser_id
        return super(Post, self).save(*args, **kwargs)
