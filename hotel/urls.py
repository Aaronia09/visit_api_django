
from rest_framework.routers import DefaultRouter
from hotel.views import hotelViewSet




router = DefaultRouter()
router.register(r'hotel', hotelViewSet,basename='hotel')

urlpatterns = [
    
]

urlpatterns+=router.urls