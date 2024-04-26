from rest_framework import serializers


class GetServiceRequestResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    profile_id = serializers.IntegerField()
    servicetype = serializers.CharField()
    manufacturer = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    asset = serializers.CharField()
    status = serializers.CharField()


class CreateServiceRequestSerializer(serializers.Serializer):
    profile_id = serializers.IntegerField()
    servicetype = serializers.CharField()
    manufacturer = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    asset = serializers.CharField()
    status = serializers.CharField()


class CreateServiceResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    profile_id = serializers.IntegerField()
    servicetype = serializers.CharField()
    manufacturer = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    asset = serializers.CharField()
    status = serializers.CharField()
