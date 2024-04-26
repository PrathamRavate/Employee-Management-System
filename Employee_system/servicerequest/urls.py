from django.urls import path
from servicerequest.views import (get_service_request,
                                  create_service_request,
                                  get_authenticate_service)

urlpatterns = [
    path('get/service/request/', get_service_request,
         name='get_service_request'),
    path('create/service/request/', create_service_request,
         name='create-service-request'),
    path('get/authenticate/service', get_authenticate_service,
         name='get_authenticate_service')
]
