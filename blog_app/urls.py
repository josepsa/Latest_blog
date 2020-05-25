from django.urls import path
from . import views

app_name='blog_app'

urlpatterns = [

    path('post_list/',views.PostListView.as_view(),name='post_lists'),
    path('post_details/<int:pk>/',views.PostDetailView.as_view(),name='post_details'),
    path('post/new',views.PostCreateView.as_view(),name='post_create'),
    path('post_drafts_list',views.PostDraftView.as_view(),name='post_drafts_list'),
    path('post_drafts_details/<int:pk>/',views.PostDraftDetailsView.as_view(),name='post_drafts_details'),
    path('post_publish/<int:pk>/publish',views.post_publish,name='post_publish'),
    path('post_comment/<int:pk>/add_comment',views.add_comment,name='add_comment'),
    path('post_update/<int:pk>/',views.PostUpdateView.as_view(),name='post_update'),
    path('post_delete/<int:pk>/',views.PostdeleteView.as_view(),name='post_delete'),
    path('comment_update/<int:pk>/',views.CommentUpdateView.as_view(),name='comment_update'),
    path('comment_remove/<int:pk>/',views.CommentRemoveView.as_view(),name='comment_delete')
]