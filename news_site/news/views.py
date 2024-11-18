from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import News, Category, Tag
from .serializers import NewsSerializer, CategorySerializer, TagSerializer

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
