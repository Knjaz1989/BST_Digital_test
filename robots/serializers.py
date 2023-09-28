from datetime import datetime

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from robots.models import Robot


class RobotCreateSerializer(serializers.ModelSerializer):
    model = serializers.CharField(max_length=2)
    version = serializers.CharField(max_length=2)
    created = serializers.DateTimeField()
    serial = serializers.CharField(read_only=True)

    class Meta:
        model = Robot
        fields = ["model", "version", "created", "serial"]
        write_only_fields = ("model", 'version', "created")


class RobotListSerializer(serializers.ModelSerializer):
    model = serializers.CharField(max_length=2)
    version = serializers.CharField(max_length=2)

    class Meta:
        model = Robot
        fields = ["model", "version"]

    def validate_created(self, value):
        if value.timestamp() > datetime.now().timestamp():
            raise ValidationError(
                "datetime can't be more than current datetime"
            )
        return value
