from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Category, Executor, Documents

User = get_user_model()


class CategorySerializer(serializers.ModelSerializer):
    """Список категорий."""

    class Meta:
        model = Category
        fields = ('id', 'name', 'color')


class ExecutorSerializer(serializers.ModelSerializer):
    """Список исполнителей."""

    class Meta:
        model = Executor
        fields = ('name',)


class DocumentsSerializer(serializers.ModelSerializer):
    """Список документов."""

    class Meta:
        model = Documents
        fields = (
            'type',
            'title',
            'number',
            'date_create',
            'pub_date',
            'executor',
            'file',
            'author',
            'under_document'
        )
