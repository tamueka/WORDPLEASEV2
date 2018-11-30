from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View

from blogs.forms import BlogForm
from blogs.models import Blog


class HomeView(View):
    def get(self, request):
        return render(request, 'blogs/home.html')


class BlogDetailView(View):
    def get(self, request, blog_pk):
        try:
                blog = Blog.objects.get(pk=blog_pk)
                context = {'blog': blog}
                return render(request, 'blogs/blog_detail.html', context)
        except Blog.DoesNotExist:
                return HttpResponse('Blog not found', status=404)


class BlogView(View):
    def get(self, request):
        # 1) Obtenemos blogs de la base de datos y los ordenamos por ultimos blogs publicados
        blogs_lista = Blog.objects.select_related('usuario').all().order_by('-fecha')
        # 2) Pasar los blogs a ala plantilla para que esta los muestre en HTML
        context = {'blogs': blogs_lista}
        return render(request, 'blogs/blogs.html', context)


class NewBlogView(View):

    @method_decorator(login_required)
    def get(self, request):
        form = BlogForm()
        return render(request, 'blogs/new_post.html', {'form': form})

    @method_decorator(login_required)
    def post(self, request):
        new_post = Blog(usuario=request.user)
        form = BlogForm(request.POST, request.FILES, instance=new_post)
        if form.is_valid():
            new_post = form.save()
            messages.success(request, 'Blog {0} created successfully!'.format(new_post.titulo))
            form = BlogForm()
        return render(request, 'blogs/new_post.html', {'form': form})