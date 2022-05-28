from django.contrib import admin
from Schedule.views import RoomViewSet, DoctorViewSet
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()  # é a rota principal
router.register('room', RoomViewSet, basename='Salas')
router.register('doctor', DoctorViewSet, basename='Médicos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('rooms/<int:pk>/', RoomViewSet.as_view),
    path('doctors/<int:pk>/', DoctorViewSet.as_view)
]