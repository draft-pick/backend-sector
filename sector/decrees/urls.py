from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router_v1 = DefaultRouter()
router_v1.register('categories', views.CategoryViewSet, basename='categories')
router_v1.register('executor', views.ExecutorViewSet, basename='executor')
router_v1.register('documents', views.DocumentViewSet, basename='documents')


urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
