from rest_framework import status
from rest_framework.generics import get_object_or_404, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from blogs.models import Blog
from blogs.serializers import BlogListSerializer, BlogSerializer


class BlogListAPIView(ListCreateAPIView):

    queryset = Blog.objects.all()

    def get_serializer_class(self):
        return BlogListSerializer if self.request.method == 'GET' else BlogSerializer


class BlogDetailAPIView(RetrieveUpdateDestroyAPIView):

    queryset = Blog.objects.all()
    serializer_class = BlogSerializer