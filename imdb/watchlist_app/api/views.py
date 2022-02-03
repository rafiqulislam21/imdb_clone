from rest_framework import status
from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.views import APIView

from watchlist_app.models import WatchList, StreamPlatform
from watchlist_app.api.serializers import WatchListSerializer, StreamPlatformSerializer

# Create your views here.

# Class based serializer---------
class StreamPlatformAV(APIView):

    def get(self, request):
        stPlatform = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(stPlatform, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class StreamPlatformDetailsAV(APIView):

    def get(self, request, pk):
        try:
            movie = StreamPlatform.objects.get(pk=pk)
            serializer = StreamPlatformSerializer(movie)
            return Response(serializer.data)
        except StreamPlatform.DoesNotExist:
            return Response({'Error': 'StreamPlatform Not found!'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            movie = StreamPlatform.objects.get(pk=pk)
            serializer = StreamPlatformSerializer(movie, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except StreamPlatform.DoesNotExist:
            return Response({'Error': 'StreamPlatform not found!'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            movie = StreamPlatform.objects.get(pk=pk)
            movie.delete()
            return Response({'response': 'StreamPlatform deleted!'}, status=status.HTTP_204_NO_CONTENT)
        except StreamPlatform.DoesNotExist:
            return Response({'Error': 'StreamPlatform not found!'}, status=status.HTTP_404_NOT_FOUND)


class WatchListAV(APIView):

    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WatchDetailsAV(APIView):
        
    def get(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
            serializer = WatchListSerializer(movie)
            return Response(serializer.data)
        except WatchList.DoesNotExist:
            return Response({'Error': 'WatchList Not found!'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
            serializer = WatchListSerializer(movie, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except WatchList.DoesNotExist:
            return Response({'Error': 'WatchList not found!'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
            movie.delete()
            return Response({'response': 'WatchList deleted!'}, status=status.HTTP_204_NO_CONTENT)
        except WatchList.DoesNotExist:
            return Response({'Error': 'WatchList not found!'}, status=status.HTTP_404_NOT_FOUND)


# Functional based serializers----------------

# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)

#     if request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_details(request, pk):
#     try:
#         movie = Movie.objects.get(pk=pk)
#         if request.method == 'GET':
#             # movie = Movie.objects.get(pk=pk)
#             serializer = MovieSerializer(movie)
#             return Response(serializer.data)

#         if request.method == 'PUT':
#             # movie = Movie.objects.get(pk=pk)
#             serializer = MovieSerializer(movie, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             else:
#                 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#         if request.method == 'DELETE':
#             # movie = Movie.objects.get(pk=pk)
#             movie.delete()
#             return Response({'response': 'Movie deleted!'}, status=status.HTTP_204_NO_CONTENT)

#     except Movie.DoesNotExist:
#         return Response({'Error': 'Movie not found!'}, status=status.HTTP_404_NOT_FOUND)
