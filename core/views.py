from django.db.models import Q
from django.shortcuts import render
from rest_framework import viewsets

from .serializer import ArticleSerializer
from .models import Article
# Create your views here.


class ArticleSviewSet(viewsets.ModelViewSet):
    model = Article
    serializer_class = ArticleSerializer
    filterset_fields ={
        "title": ["icontains", ], 
    }

    def get_queryset(self):
        search = self.request.query_params.get("search", '')
        return self.model.objects.filter(Q(title__icontains=search) | Q(body__icontains=search))
