from django.urls import path
from django.conf.urls import url
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='my_app-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='my_app-about'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    #path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    #path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
    #url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    #url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    #url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    #url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    #url(r'^post/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='post_detail'),
]
