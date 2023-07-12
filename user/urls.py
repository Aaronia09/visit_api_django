
from django.urls import path
from rest_framework.routers import DefaultRouter
from user.views import userViewSet

router = DefaultRouter()
router.register(r'user', userViewSet,basename='user')

urlpatterns = [
    
]

urlpatterns+=router.urls