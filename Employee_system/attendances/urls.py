from django.urls import path
from attendances.views import (get_all_attendance, create_attendance,
                               get_attendance, check_attendance_status)

urlpatterns = [
    path('get_all_attendance/', get_all_attendance, name='get_all_attendance'),
    path('create_attendance/', create_attendance, name='create_attendance'),
    path('get/attendance/', get_attendance, name='get_attendance'),
    path('check/attendance/status/<int:profile_id>/',
         check_attendance_status, name='check_attendance_status')

]
