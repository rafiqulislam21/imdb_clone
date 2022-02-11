from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import (WatchListAV, WatchDetailsAV, 
                                     StreamPlatformAV, StreamPlatformDetailsAV, 
                                     ReviewList, ReviewDetails, ReviewCreate,
                                     StreamPlatformVS, userReview, WatchListGV)

router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')
urlpatterns = [
    # path('', Home, name='home'),
    path('filter/', WatchListGV.as_view(), name='watch-list-filter'),

    path('list/', WatchListAV.as_view(), name='watch-list'),
    path('<int:pk>/', WatchDetailsAV.as_view(), name='watch-details'),
    path('', include(router.urls)),
    # path('stream/', StreamPlatformAV.as_view(), name='stream'),
    # path('stream/<int:pk>', StreamPlatformDetailsAV.as_view(),name='stream-platform-details'),
    
    # path('review/', ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>', ReviewDetails.as_view(), name='review-details'),
    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/reviews/', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>/', ReviewDetails.as_view(), name='review-details'),
    
    # path('reviews/<str:username>/', userReview.as_view(), name='user-review-list'),
    path('reviews/', userReview.as_view(), name='user-review-list'),
]
