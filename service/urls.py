

from django.urls import path
from rest_framework.routers import DefaultRouter
from service.views import serviceViewSet


router = DefaultRouter()
router.register(r'service', serviceViewSet,basename='service')

urlpatterns = [
    
]

urlpatterns+=router.urls