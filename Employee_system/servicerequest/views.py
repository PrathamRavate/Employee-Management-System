from rest_framework.decorators import (api_view, authentication_classes,
                                       permission_classes)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import ServiceRequest
from django.utils import timezone
from datetime import datetime, timedelta
from django.utils import timezone
from servicerequest.serializers import (GetServiceRequestResponseSerializer,
                                        CreateServiceRequestSerializer,
                                        CreateServiceResponseSerializer)


@api_view(['GET'])
def get_service_request(request):
    response_serializer = ServiceRequest.objects.all()
    serializer = GetServiceRequestResponseSerializer(response_serializer,
                                                     many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_service_request(request):
    request_serializer = CreateServiceRequestSerializer(data=request.data)
    if request_serializer.is_valid():
        service = ServiceRequest.objects.create(
            profile_id=request_serializer.validated_data.get('profile_id'),
            servicetype=request_serializer.validated_data.get('servicetype'),
            manufacturer=request_serializer.validated_data.get('description'),
            title=request_serializer.validated_data.get('title'),
            description=request_serializer.validated_data.get('description'),
            asset=request_serializer.validated_data.get('asset'),
            status='3'
        )
        response_serializer = CreateServiceResponseSerializer(service)
        return Response(response_serializer.data, status=status.HTTP_200_OK)
    return Response(request_serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_authenticate_service(request):
    current_user = request.user.profile
    request_objects = ServiceRequest.objects.filter(profile=current_user)
    response_serializer = GetServiceRequestResponseSerializer(request_objects,
                                                              many=True)
    return Response(response_serializer.data, status=status.HTTP_200_OK)
