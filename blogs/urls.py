from django.urls import path

from blogs.views import home, blog_detail, blogs, new_post

urlpatterns = [
    path('blogs', blogs, name='blogs'),
    path('blogs/<int:blog_pk>', blog_detail, name='blog_detail'),
    path('new_post', new_post, name='new_post'),
    path('', home, name='home')
]