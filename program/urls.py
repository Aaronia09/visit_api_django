

from django.urls import path
from rest_framework.routers import DefaultRouter
from program.views import programViewSet




router = DefaultRouter()
router.register(r'program', programViewSet,basename='program')

urlpatterns = [

]

urlpatterns+=router.urls