from rest_framework.response import Response
from rest_framework.decorators import (api_view, permission_classes,
                                       authentication_classes)
from attendances.serializers import (GetAttendanceResponseSerializer,
                                     GetAttendancelogicSerializer,
                                     CreateAttendanceRequestSerializer,
                                     CreateAttendanceResponseSerializer)
from rest_framework import status as Status
from attendances.models import Attendance
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from datetime import datetime, time
from attendances.permissions import (
    LeaveBasicPermission
)
# Create your views here.


@api_view(['GET'])
def get_all_attendance(request):
    attendance_objects = Attendance.objects.all()
    serializer = GetAttendanceResponseSerializer(attendance_objects, many=True)
    return Response(serializer.data, status=Status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([LeaveBasicPermission])
def create_attendance(request):
    request_serializer = CreateAttendanceRequestSerializer(data=request.data)
    if request_serializer.is_valid():
        attendance = Attendance.objects.create(
            profile_id=request_serializer.validated_data.get('profile_id'),
            date=request_serializer._validated_data.get('date'),
            time_in=request_serializer.validated_data.get('time_in'),
            time_out=request_serializer.validated_data.get('time_out'),
            status='3'
        )
        response_serializer = CreateAttendanceResponseSerializer(attendance)
        return Response(response_serializer.data,
                        status=Status.HTTP_201_CREATED)
    return Response(request_serializer.errors,
                    status=Status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_attendance(request):
    current_user = request.user.profile
    getattendance = Attendance.objects.filter(profile=current_user)
    serializer = CreateAttendanceResponseSerializer(getattendance, many=True)
    return Response(serializer.data,
                    status=Status.HTTP_200_OK)


@api_view(['GET'])
def check_attendance_status(request, profile_id):
    today = datetime.now().date()
    attendance_exist = Attendance.objects.filter(profile_id=profile_id,
                                                 date=today).exists()
    if not attendance_exist:
        attendance_status = "Employee is absent"
    else:
        attendance_today = Attendance.objects.get(profile_id=profile_id,
                                                  date=today)
        time_in = attendance_today.time_in
        if time(9, 0) <= time_in <= time(10, 0):
            attendance_status = "Present"
        elif time_in > time(10, 0):
            attendance_status = "Late"
        else:
            attendance_status = "Employee is absent"

    serializer = GetAttendancelogicSerializer({'attendance_status':
                                               attendance_status})
    return Response(serializer.data)
