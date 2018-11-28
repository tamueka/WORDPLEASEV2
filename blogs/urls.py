from django.urls import path

from blogs.views import BlogView, BlogDetailView, NewBlogView, HomeView

urlpatterns = [
    path('blogs', BlogView.as_view(), name='blogs'),
    path('blogs/<int:pk>', BlogDetailView.as_view(), name='blog_detail'),
    path('new_post', NewBlogView.as_view(), name='new_post'),
    path('', HomeView.as_view(), name='home')
]
