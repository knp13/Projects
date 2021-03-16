from django.urls import path
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView
from . import views


urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
]

#pip install crispy forms
