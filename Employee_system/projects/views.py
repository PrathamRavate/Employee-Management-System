from rest_framework.response import Response
from rest_framework import status as Status
from rest_framework.decorators import (api_view, authentication_classes,
                                       permission_classes)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from projects.models import Project
from projects.serializers import (getprojectresponseserializer,
                                  Requestcreateprojectserializer,
                                  Responsecreateprojectserializer)


@api_view(['GET'])
def get_project_list(request):
    projects_list = Project.objects.all()
    serializer = getprojectresponseserializer(projects_list, many=True)
    return Response(serializer.data, status=Status.HTTP_200_OK)


@api_view(['POST'])
def create_project(request):
    request_serializer = Requestcreateprojectserializer(data=request.data)
    if request_serializer.is_valid():
        project = Project.objects.create(
            name=request_serializer.validated_data.get('name'),
            project_type=request_serializer.validated_data.get('project_type'),
            profile_id=request_serializer.validated_data.get('profile_id'),
            start_date=request_serializer.validated_data.get('start_date'),
            end_date=request_serializer.validated_data.get('end_date'),
            completed=request_serializer.validated_data.get('completed'),
            project_description=request_serializer.validated_data.get
            ('project_description'),
            execution_type=request_serializer.validated_data.get
            ('execution_type'),
        )
        response_serializer = Responsecreateprojectserializer(project)
        return Response(response_serializer.data,
                        status=Status.HTTP_201_CREATED)
    return Response(request_serializer.errors,
                    status=Status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_specific_project(request):
    current_user = request.user.profile
    project_list = Project.objects.filter(profile=current_user)
    serializer = getprojectresponseserializer(project_list, many=True)
    return Response(serializer.data, status=Status.HTTP_200_OK)
