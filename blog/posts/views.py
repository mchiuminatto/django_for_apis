from django.shortcuts import render
from rest_framework import permissions # new
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Post
from .serializer import PostSerializer
# Create your views here.


class PostList(ListCreateAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetails(RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser, )  # new
    queryset = Post.objects.all()
    serializer_class = PostSerializer


