from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from blogs.models import Blog
from blogs.permissions import BlogPermission #permisos creados por nosotros
from blogs.serializers import BlogListSerializer, BlogSerializer


class BlogListAPIView(ListCreateAPIView):

    queryset = Blog.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Blog.objects.all() if self.request.user.is_authenticated else Blog.objects.all().filter(publicado=Blog.PUBLICADO)

    def get_serializer_class(self):
        return BlogListSerializer if self.request.method == 'GET' else BlogSerializer

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


class BlogDetailAPIView(RetrieveUpdateDestroyAPIView):

    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [BlogPermission]
