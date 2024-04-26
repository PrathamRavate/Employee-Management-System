from rest_framework import serializers


class GetPerformanceResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    profile = serializers.CharField()
    date = serializers.DateField()
    comments = serializers.CharField()
    ratings = serializers.CharField()


class CreateReviewsRequestSerializer(serializers.Serializer):
    profile_id = serializers.IntegerField()
    date = serializers.DateField()
    comments = serializers.CharField()
    ratings = serializers.CharField()


class CreateReviewsResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    profile_id = serializers.IntegerField()
    date = serializers.DateField()
    comments = serializers.CharField()
    ratings = serializers.CharField()
