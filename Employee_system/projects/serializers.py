from rest_framework import serializers


class getprojectresponseserializer(serializers.Serializer):
    name = serializers.CharField()
    project_type = serializers.CharField()
    profile = serializers.CharField()
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    completed = serializers.BooleanField()
    project_description = serializers.CharField()
    execution_type = serializers.CharField()


class Requestcreateprojectserializer(serializers.Serializer):
    name = serializers.CharField()
    project_type = serializers.CharField()
    profile_id = serializers.IntegerField()
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    completed = serializers.BooleanField()
    project_description = serializers.CharField()
    execution_type = serializers.CharField()


class Responsecreateprojectserializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    project_type = serializers.CharField()
    profile_id = serializers.IntegerField()
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    completed = serializers.BooleanField()
    project_description = serializers.CharField()
    execution_type = serializers.CharField()
