from django.urls import path
from performancereviews.views import (getperformancereview, createreview,
                                      get_authenticate_review)

urlpatterns = [
    path('get/performance/review', getperformancereview,
         name='get-performance-review'),
    path('create/review', createreview, name='create-review'),
    path('get/authenticate/review', get_authenticate_review,
         name='get/authenticate/review'),
]
