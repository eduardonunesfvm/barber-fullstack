from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from appointments.models import Appointment
from .serializers import AppointmentSerializer

class AppointmentViewSet(ModelViewSet):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Appointment.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)