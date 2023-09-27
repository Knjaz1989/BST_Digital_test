from rest_framework import serializers

from robots.models import Robot


class RobotSerializer(serializers.ModelSerializer):
    model = serializers.CharField(max_length=2)
    version = serializers.CharField(max_length=2)
    created = serializers.DateTimeField()
    serial = serializers.CharField(read_only=True)

    class Meta:
        model = Robot
        fields = ["model", "version", "created", "serial"]
        write_only_fields = ("model", 'version', "created")
