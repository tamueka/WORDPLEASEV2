from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from blogs.forms import BlogForm
from blogs.models import Blog


def home(request):

    return render(request, 'blogs/home.html')

def blog_detail(request, blog_pk):
    try:
        blog = Blog.objects.get(pk=blog_pk)
        context = {'blog': blog}
        return render(request, 'blogs/blog_detail.html', context)
    except Blog.DoesNotExist:
        return HttpResponse('Blog not found', status=404)

def blogs(request):
    # 1) Obtenemos blogs de la base de datos y los ordenamos por ultimos blogs publicados
    blogs_lista = Blog.objects.select_related('usuario').all().order_by('-fecha')

    # 2) Pasar los blogs a a la plantilla para que esta los muestre en HTML
    context = {'blogs': blogs_lista}
    return render(request, 'blogs/blogs.html', context)


@login_required
def new_post(request):
    if request.method == 'POST':
        new_post = Blog(usuario=request.user)
        form = BlogForm(request.POST, request.FILES, instance=new_post)
        if form.is_valid():
            new_post = form.save()
            messages.success(request, 'Blog {0} created successfully!'.format(new_post.titulo))
            form = BlogForm()
    else:
        form = BlogForm()

    return render(request, 'blogs/new_post.html', {'form': form})