from django.urls import path
from employee_profiles.views import get_profile_all , create_profile  , getonlyleaverange , get_all_leaves , get_leave_range , create_leave ,get_leave ,obtain_auth_token, get_leave_currentmonth, get_leave_year

urlpatterns = [
    path('get_all_profiles/', get_profile_all, name='get_profile_all'),
    path('create_profiles/' , create_profile , name = 'create_profile'),
    path('get_all_leaves/' , get_all_leaves , name = 'get_all_leaves'),
    path('create_leave/' , create_leave , name = 'create_leave'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('get_leave/' , get_leave , name = 'get_leave'),
    path('get_leave_range/' , get_leave_range , name = 'get_leave_range'),
    path('getonlyleaverange/' , getonlyleaverange , name = 'getonlyleaverange'),
    path('get/leave/currentmonth/', get_leave_currentmonth, name='get_leave_currentmonth'),
    path('get/leave/year/', get_leave_year, name='get_leave_year')

]