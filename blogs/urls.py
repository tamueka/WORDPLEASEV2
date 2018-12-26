from django.urls import path

from blogs.api import BlogListAPIView, BlogDetailAPIView
from blogs.views import BlogView, BlogDetailView, NewBlogView, HomeView



urlpatterns = [
    path('blogs', BlogView.as_view(), name='blogs'),
    path('blogs/<int:blog_pk>', BlogDetailView.as_view(), name='blog_detail'),
    path('new_post', NewBlogView.as_view(), name='new_post'),
    path('', HomeView.as_view(), name='home'),

    # API
    path('api/1.0/blogs/', BlogListAPIView.as_view(), name='blog_list_api'),
    path('api/1.0/blogs/<int:pk>', BlogDetailAPIView.as_view(), name='blog_detail_api')
]