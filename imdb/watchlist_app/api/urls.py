from django.urls import path, include
# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import (WatchListAV, WatchDetailsAV, 
                                     StreamPlatformAV, StreamPlatformDetailsAV, 
                                     ReviewList, ReviewDetails)

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='watch-list'),
    path('<int:pk>', WatchDetailsAV.as_view(), name='watch-details'),
    path('stream/', StreamPlatformAV.as_view(), name='stream'),
    path('stream/<int:pk>', StreamPlatformDetailsAV.as_view(),
         name='stream-platform-details'),
    path('review/', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>', ReviewDetails.as_view(), name='review-details'),
    # path('list/', movie_list, name='movie-list'),
    # path('<int:pk>', movie_details, name='movie-details'),
    # path('api-auth/', include('rest_framework.urls'))
]
