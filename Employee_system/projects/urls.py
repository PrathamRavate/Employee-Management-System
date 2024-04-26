from django.urls import path
from projects.views import (get_project_list, create_project,
                            get_specific_project)

urlpatterns = [
    path('get_project_list/', get_project_list, name='get_project_list'),
    path('create_project/', create_project, name='create_project'),
    path('get_specific_project/', get_specific_project,
         name='get_specific_project')
]
