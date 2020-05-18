from django.contrib.auth import mixins
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.utils import timezone

from django.views import generic
from . import models
from . import forms

from django.contrib.auth import models as auth_model

from crum import get_current_user





class PostListView(generic.ListView):
    model = models.Post
    template_name = 'blog_app/post_lists.html'

    def get_queryset(self):
        return models.Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(generic.DetailView):
    model = models.Post
    template_name = 'blog_app/post_details.html'


class PostCreateView(generic.CreateView,mixins.LoginRequiredMixin):
    model = models.Post
    template_name = 'blog_app/post_create.html'
    form_class = forms.PostForm


class PostDraftView(generic.ListView):
    model=models.Post
    template_name = 'blog_app/post_drafts.html'
    current_user = get_current_user()

    def get_queryset(self):
        #return models.Post.objects.filter(author=auth_model.User.User.username).order_by('-created_date')
        return models.Post.objects.order_by('-created_date')


class PostDraftDetailsView(generic.DetailView):
    model = models.Post
    template_name = 'blog_app/post_draft_details.html'

