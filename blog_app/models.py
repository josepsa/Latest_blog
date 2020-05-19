
from django.contrib.auth import get_user_model
from django.db import models
from crum import get_current_user

# Create your models here.
from django.urls import reverse
from django.utils import timezone

User=get_user_model()

class Post(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,default=None)
    title = models.CharField(max_length=150)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_app:post_details',kwargs={'pk':self.pk})

    def save(self,*args,**kwargs):
        current_user=get_current_user()
        if current_user and not User.pk:
            current_user=None
        if not self.pk:
            self.author=current_user
        super(Post,self).save(*args,**kwargs)

    def publish(self):
        self.published_date=timezone.now()
        self.save()


class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,blank=True,null=True)
    text=models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,default=None)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('blog_app:post_details',kwargs={'pk':self.pk})

    def save(self,*args,**kwargs):
        current_user=get_current_user()
        if current_user and not User.pk:
            current_user=None
        if not self.pk:
            self.created_by=current_user
        super(Comment,self).save(*args,**kwargs)

