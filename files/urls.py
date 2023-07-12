
from rest_framework.routers import DefaultRouter

from files.views import FilesViewSet




router = DefaultRouter()
router.register(r'files', FilesViewSet,basename='files')

urlpatterns = [
    
]

urlpatterns+=router.urls