from datetime import datetime, timedelta
from tempfile import NamedTemporaryFile

from django.db.models import Count
from django.http import HttpResponse
from django.views import View
from rest_framework import viewsets, mixins

from robots.models import Robot
from robots import serializers as robot_sr
from robots.utils import create_xlsx


class RobotsViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = Robot.objects.all()
    serializer_class = robot_sr.RobotCreateSerializer

    def perform_create(self, serializer):
        serial = f'{serializer.validated_data["model"]}-' \
                 f'{serializer.validated_data["model"]}'
        serializer.save(serial=serial)


class StatisticView(View):

    def get(self, request, *args, **kwargs):
        current_date = datetime.now().date()
        start_date = (
            current_date - timedelta(days=7)
        )
        result = Robot.objects.values("model", "version").filter(
            created__gte=start_date
        ).annotate(total=Count('id'))
        robots_group = {}
        for item in result:
            model = item.pop("model")
            robots_group[model] = robots_group.get(model, []) + [item]
        with NamedTemporaryFile(suffix=".xlsx") as tmp:
            create_xlsx(tmp.name, robots_group)
            tmp.seek(0)
            response = HttpResponse(
                tmp.read(),
                content_type='application/ms-excel',
            )
            filename = f"statistic_{start_date}-{current_date}.xlsx"
            response[
                'Content-Disposition'] = f'attachment; filename="{filename}"'
        return response
