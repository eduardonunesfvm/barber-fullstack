from rest_framework.routers import DefaultRouter
from .viewsets import AppointmentViewSet

router = DefaultRouter()
router.register(r'', AppointmentViewSet)

urlpatterns = router.urls