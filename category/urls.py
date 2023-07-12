
from django.urls import path
from rest_framework.routers import DefaultRouter
from category.views import categoryViewSet




router = DefaultRouter()
router.register(r'category', categoryViewSet,basename='category')

urlpatterns = [
    
]

urlpatterns+=router.urls