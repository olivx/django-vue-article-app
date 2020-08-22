from django.shortcuts import render
from rest_framework import viewsets

from .serializer import ArticleSerializer
from .models import Article
# Create your views here.


class ArticleSviewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

