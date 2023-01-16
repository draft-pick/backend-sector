from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import viewsets
from .mixins import CreateListDestroyModelViewSet
from .models import Category, Executor, Documents
from .serializers import (
    CategorySerializer, ExecutorSerializer, DocumentsSerializer
)
from .permissions import IsAdminOrReadOnly


class CategoryViewSet(viewsets.ModelViewSet):
    """Получаем список категорий."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = [
    #     IsAdminOrReadOnly,
    # ]
    search_fields = ['=name']


class ExecutorViewSet(viewsets.ModelViewSet):
    """Получаем список исполнителей."""
    queryset = Executor.objects.all()
    serializer_class = ExecutorSerializer
    # permission_classes = [
    #     IsAdminOrReadOnly,
    # ]
    search_fields = ['=name']


class DocumentViewSet(viewsets.ModelViewSet):
    """Получаем список документов."""
    queryset = Documents.objects.all()
    serializer_class = DocumentsSerializer
    # permission_classes = [
    #     IsAdminOrReadOnly,
    # ]
    search_fields = ['=title', '=number']
