from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ResourceViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'resources', ResourceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]