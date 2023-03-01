from rest_framework import generics

from blog.models import Post
from .serializers import PostSerializer


class PostListCreate(generics.ListCreateAPIView):
	queryset = Post.objects.posts_public()
	serializer_class = PostSerializer


class PostDetailsDelete(generics.RetrieveDestroyAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer 
	lookup_field = 'pk'