
from rest_framework.routers import DefaultRouter
from category.views import categoryViewSet
from favorites.views import favoritesViewSet
from files.views import filesViewSet
from hotel.views import cityViewSet, hotelViewSet, roomtypeViewSet
from program.views import programViewSet
from service.views import accessibilitiesViewSet, serviceViewSet
from user.views import userViewSet

router = DefaultRouter()
router.register(r'category', categoryViewSet, basename='category')
router.register(r'user', userViewSet, basename='user')
router.register(r'hotel', hotelViewSet, basename='hotel')
router.register(r'files', filesViewSet, basename='files')
router.register(r'city', cityViewSet, basename='city')
router.register(r'service', serviceViewSet, basename='service')
router.register(r'roomtype', roomtypeViewSet, basename='roomtype')

router.register(r'accessibilities', accessibilitiesViewSet, basename='accessibilities')
router.register(r'program', programViewSet, basename='program')
router.register(r'favorites' ,favoritesViewSet, basename='favorites')


urlpatterns = [
    # Autres routes URL de votre application
]

urlpatterns += router.urls
