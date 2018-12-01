from rest_framework import serializers

from blogs.models import Blog


class BlogListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = ['id', 'titulo', 'texto', 'url']


class BlogSerializer(BlogListSerializer):

    class Meta(BlogListSerializer.Meta):

        fields = '__all__'
        read_only_fields = ['usuario']