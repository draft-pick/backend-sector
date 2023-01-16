from django.db import models
from django.contrib.auth import get_user_model
from uuid import uuid4

import datetime as dt
import os

User = get_user_model()

current = dt.datetime.now()


class Category(models.Model):
    name = models.CharField(max_length=255,
                            verbose_name='Название категории')
    color = models.CharField(
        max_length=7,
        verbose_name="Цвет в HEX",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'



class Executor(models.Model):
    """Исполнители."""
    name = models.CharField("ФИО", max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'


class Documents(models.Model):
    """Приказы"""
    type = models.ForeignKey(
        Category,
        verbose_name="Тип документа",
        null=True,
        on_delete=models.SET_NULL,
        related_name="type_document",
        blank=True,
    )
    title = models.CharField("Название", max_length=500)
    number = models.IntegerField("Номер", null=True)
    date_create = models.DateField(null=True)
    pub_date = models.DateField(auto_now_add=True)
    executor = models.ForeignKey(
        Executor,
        on_delete=models.CASCADE,
        related_name='executor_document',
        blank=True,
        null=True,
    )
    file = models.FileField(
        blank=False,
        upload_to=(f"documents/{current.year}/{current.month}"),
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='author_document',
        null=True,
    )
    under_document = models.ForeignKey('self',
                                       on_delete=models.CASCADE,
                                       related_name='main_document',
                                       null=True,
                                       blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'
