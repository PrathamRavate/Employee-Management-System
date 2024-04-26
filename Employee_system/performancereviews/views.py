from performancereviews.models import Review
from performancereviews.serializers import (GetPerformanceResponseSerializer,
                                            CreateReviewsRequestSerializer,
                                            CreateReviewsResponseSerializer)
from rest_framework import status as Status
from rest_framework.decorators import (api_view, authentication_classes,
                                       permission_classes)
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
def getperformancereview(request):
    review_objects = Review.objects.all()
    serializer = GetPerformanceResponseSerializer(review_objects, many=True)
    return Response(serializer.data, status=Status.HTTP_201_CREATED)


@api_view(['POST'])
def createreview(request):
    request_serializer = CreateReviewsRequestSerializer(data=request.data)
    if request_serializer.is_valid():
        performance = Review.objects.create(
            profile_id=request_serializer.validated_data.get('profile_id'),
            date=request_serializer.validated_data.get('date'),
            comments=request_serializer.validated_data.get('comments'),
            ratings=request_serializer.validated_data.get('ratings'),
        )
        response_serializer = CreateReviewsResponseSerializer(performance)
        return Response(response_serializer.data,
                        status=Status.HTTP_201_CREATED)
    return Response(request_serializer.errors,
                    status=Status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_authenticate_review(request):
    current_user = request.user.profile
    performance = Review.objects.filter(profile=current_user)
    serializer = GetPerformanceResponseSerializer(performance, many=True)
    return Response(serializer.data, status=Status.HTTP_201_CREATED)
