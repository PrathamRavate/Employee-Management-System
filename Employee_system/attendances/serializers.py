from rest_framework import serializers


class GetAttendanceResponseSerializer(serializers.Serializer):
    profile = serializers.CharField()
    date = serializers.DateField()
    time_in = serializers.TimeField()
    time_out = serializers.TimeField()
    status = serializers.CharField()


class CreateAttendanceRequestSerializer(serializers.Serializer):
    profile_id = serializers.CharField()
    date = serializers.DateField()
    time_in = serializers.TimeField()
    time_out = serializers.TimeField()
    status = serializers.CharField()


class CreateAttendanceResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    profile_id = serializers.CharField()
    date = serializers.DateField()
    time_in = serializers.TimeField()
    time_out = serializers.TimeField()
    status = serializers.CharField()


class GetAttendancelogicSerializer(serializers.Serializer):
    attendance_status = serializers.CharField()
