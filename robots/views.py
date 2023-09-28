from rest_framework import viewsets, mixins

from robots.models import Robot
from robots.serializers import RobotSerializer


class RobotsViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = Robot.objects.all()
    serializer_class = RobotSerializer

    def perform_create(self, serializer):
        serial = f'{serializer.validated_data["model"]}-' \
                 f'{serializer.validated_data["model"]}'
        serializer.save(serial=serial)
