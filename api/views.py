from django.shortcuts import render
from . models import Blog
from .serializers import BlogSerializer
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,RetrieveAPIView
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import viewsets
# Create your views here.

class BlogListView(ListAPIView):
    queryset = Blog.objects.order_by('-date_created')
    serializer_class = BlogSerializer
    lookup_field='slug'
    # permission_classes=(permissions.AllowAny,)

class BlogDetailView(RetrieveAPIView):
    queryset = Blog.objects.order_by('-date_created')
    serializer_class = BlogSerializer
    lookup_field='slug'
    # permission_classes=(permissions.AllowAny)

class BlogFeaturedView(ListAPIView):
    queryset = Blog.objects.all().filter(featured=True)
    serializer_class = BlogSerializer
    lookup_field='slug'
    # permission_classes=(permissions.AllowAny)

class BlogCategoryView(APIView):
    serializer_class = BlogSerializer
    # permission_classes=(permissions.AllowAny)

    def post(self,*args,**kwargs):
        data=self.request.data
        category=data['category']
        queryset = Blog.objects.order_by('-date_created').filter(category__iexact=category)

        serializer =BlogSerializer(queryset,many=True)

        return Response(serializer.data)
