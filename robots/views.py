from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from rest_framework import viewsets, mixins

from robots.models import Robot
from robots.serializers import RobotSerializer


# Create your views here.

# @require_http_methods(["POST"])
class RobotsViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = Robot.objects.all()
    serializer_class = RobotSerializer

    def perform_create(self, serializer):
        serial = f'{serializer.validated_data["model"]}-{serializer.validated_data["model"]}'
        serializer.save(serial=serial)
