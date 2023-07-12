

from django.urls import path
from rest_framework.routers import DefaultRouter
from pack.views import packViewSet




router = DefaultRouter()
router.register(r'pack', packViewSet,basename='pack')

urlpatterns = [

]

urlpatterns+=router.urls