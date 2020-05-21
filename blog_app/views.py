from django.contrib.auth import mixins
from django.contrib.auth import decorators
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils import timezone

from django.views import generic
from . import models
from . import forms


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

    def get_queryset(self):
        return models.Post.objects.filter(author=self.request.user).order_by('-created_date')



class PostDraftDetailsView(generic.DetailView):
    model = models.Post
    template_name = 'blog_app/post_draft_details.html'


@decorators.login_required
def post_publish(request,pk):
    post=get_object_or_404(models.Post,pk=pk)
    post.publish()
    return redirect('blog_app:post_details',pk=pk)

@decorators.login_required
def add_comment(request,pk):
    post_name=get_object_or_404(models.Post,pk=pk)
    if request.method=='POST':
        form=forms.CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post_name
            comment.save()
            return redirect('blog_app:post_details',pk=post_name.pk)
    else:
        form=forms.CommentForm
        return render(request, 'blog_app/add_comment.html', {'form': form})  #this if for the GET request to return form


class PostUpdateView(mixins.LoginRequiredMixin,generic.UpdateView):
    model = models.Post
    template_name = 'blog_app/post_update.html'
    form_class = forms.PostForm
    #redirect_field_name = 'blog_app/post_details.html'

class PostdeleteView(mixins.LoginRequiredMixin,generic.DeleteView):
    model = models.Post
    template_name = 'blog_app/post_delete.html'
    success_url = reverse_lazy('blog_app:post_lists')



