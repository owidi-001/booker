from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'passenger', PassengerViewSet, basename='passenger')
router.register(r'driver', DriverViewSet, basename='driver')
router.register(r'bus', BusViewSet, basename='bus')
router.register(r'routes', RoutesViewSet, basename='routes')
router.register(r'booking', BookingViewSet, basename='booking')

urlpatterns = [
    path('', include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework'))
]