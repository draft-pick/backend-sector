from django.contrib import admin

from .models import Category, Executor, Documents


admin.site.register(Category)

admin.site.register(Executor)

admin.site.register(Documents)
