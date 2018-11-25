"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from blogs.views import home, blog_detail, blogs, new_post
from users.views import login, logout, signup


urlpatterns = [
    path('admin/', admin.site.urls),

    path('blogs', blogs, name='blogs'),

    path('blogs/<int:blog_pk>', blog_detail, name='blog_detail'),

    path('new_post', new_post, name='new_post'),

    path('login', login, name='login'),

    path('logout', logout, name='logout'),

    path('signup', signup, name='signup'),

    path('', home, name='home')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
