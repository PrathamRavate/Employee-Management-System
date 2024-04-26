from rest_framework.response import Response
from rest_framework.decorators import (api_view, permission_classes,
                                       authentication_classes)
from rest_framework import status as Status
from employee_profiles.models import Profile, Leave
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from employee_profiles.serializers import (GetAllEmployeeProfileSerializer,
                                           GetLeaveRangeRequestSerializer,
                                           GetleaveResponseserializer,
                                           CreateProfileRequestSerializer,
                                           CreateProfileResponseSerializer,
                                           GetAllleaveResponseserializer,
                                           CreateLeaveRequestSerializer,
                                           CreateLeaveResponseSerializer)
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from employee_profiles.serializers import AuthTokenSerializer
from rest_framework import status
from datetime import datetime, timedelta


@api_view(['GET'])
def get_profile_all(request):
    profile_objects = Profile.objects.all()
    serializer = GetAllEmployeeProfileSerializer(profile_objects, many=True)
    return Response(serializer.data,
                    status=Status.HTTP_200_OK)


@api_view(['POST'])
def create_profile(request):
    request_serializer = CreateProfileRequestSerializer(data=request.data)
    if request_serializer.is_valid():
        profile = Profile.objects.create(
            name=request_serializer.validated_data.get('name'),
            email=request_serializer.validated_data.get('email'),
            contact=request_serializer.validated_data.get('contact'),
            joining_date=request_serializer.validated_data.get('joining_date'),
            salary=request_serializer.validated_data.get('salary'),
            address=request_serializer.validated_data.get('address'),
            department=request_serializer.validated_data.get('department'),
            position=request_serializer.validated_data.get('position')
        )
        response_serialier = CreateProfileResponseSerializer(profile)
        return Response(response_serialier.data,
                        status=Status.HTTP_201_CREATED)
    return Response(request_serializer.errors,
                    status=Status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_all_leaves(request):
    leave_objects = Leave.objects.all()
    serializer = GetAllleaveResponseserializer(leave_objects, many=True)
    return Response(serializer.data, status=Status.HTTP_200_OK)


@api_view(['POST'])
def create_leave(request):
    request_serializer = CreateLeaveRequestSerializer(data=request.data)
    if request_serializer.is_valid():
        leave = Leave.objects.create(
            profile_id=request_serializer.validated_data.get('profile_id'),
            leave_type=request_serializer.validated_data.get('leave_type'),
            start_date=request_serializer.validated_data.get('start_date'),
            end_date=request_serializer.validated_data.get('end_date'),
            reason=request_serializer.validated_data.get('reason'),
            status='3'
        )
        response_serializer = CreateLeaveResponseSerializer(leave)
        return Response(response_serializer.data,
                        status=Status.HTTP_201_CREATED)
    return Response(request_serializer.errors,
                    status=Status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def obtain_auth_token(request):
    if request.method == 'POST':
        serializer = AuthTokenSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(request=request,
                                username=serializer.validated_data['username'],
                                password=serializer.validated_data['password'])
            if user:
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key})
            else:
                return Response({'error': 'Invalid credentials'},
                                status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_leave(request):
    current_user = request.user.profile
    getprofile = Leave.objects.filter(profile=current_user)
    serializer = GetleaveResponseserializer(getprofile, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_leave_range(request):
    serializer = GetLeaveRangeRequestSerializer(data=request.query_params)
    if serializer.is_valid():
        leave_start_date = serializer.validated_data.get('start_date')
        leave_end_date = serializer.validated_data.get('end_date')

        leave_objects = Leave.objects.filter(profile=request.user.profile,
                                             start_date__gte=leave_start_date,
                                             end_date__lte=leave_end_date)
        serializer = CreateLeaveResponseSerializer(leave_objects, many=True)
        return Response(serializer.data)
    return Response(serializer.errors,
                    status=Status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getonlyleaverange(request):
    serializer = GetLeaveRangeRequestSerializer(data=request.query_params)
    if serializer.is_valid():
        leave_start_date = serializer.validated_data.get('start_date')
        end_leave_date = serializer.validated_data.get('end_date')

        leave_objects = Leave.objects.filter(start_date__gte=leave_start_date,
                                             end_date__lte=end_leave_date)
        Serializer = CreateLeaveResponseSerializer(leave_objects, many=True)
        return Response(Serializer.data)


@api_view(['GET'])
def get_leave_currentmonth(request):
    current_date = datetime.now()
    current_year = current_date.year
    current_month = current_date.month
    current_month_leaves = Leave.objects.filter(
        start_date__year=current_year,
        start_date__month=current_month
    )
    serializer = CreateLeaveResponseSerializer(current_month_leaves, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_leave_year(request):
    current_datetime = datetime.now()
    past_year = current_datetime.date() - timedelta(days=365)
    past_year_leaves = Leave.objects.filter(start_date__gte=past_year)
    serializer = CreateLeaveResponseSerializer(past_year_leaves, many=True)
    return Response(serializer.data)




