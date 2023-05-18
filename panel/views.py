from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated

from django.db.models import Q
from datetime import date, timedelta

from . import serializers
from . import models

from .permission import IsAdmin


class SliderCreatView(APIView):
    permission_classes = [IsAdmin]
    
    def post(self, request, *args, **kwargs):
        serializer = serializers.SliderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class SliderRetrieveView(APIView):
    permission_classes = [IsAdmin]

    def get(self, request):
        queryset = models.Slider.objects.all()
        serializer = serializers.SliderSerializer(instance=queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SliderDelView(APIView):
    permission_classes = [IsAdmin]

    def delete(self, request, pk):
        queryset = models.Slider.objects.get(pk=pk)
        queryset.delete()
        return Response({'deleted'}, status=status.HTTP_200_OK)
    

class EventCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAdmin]
    queryset = models.EventModel.objects.all()
    serializer_class = serializers.EventModelSerializer


class EventGpdView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdmin]
    queryset = models.EventModel.objects.all()
    serializer_class = serializers.EventModelSerializer


class AudioCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAdmin]
    queryset = models.AudioModel.objects.all()
    serializer_class = serializers.AudioModelSerializer


class AudioGpdView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdmin]
    queryset = models.AudioModel.objects.all()
    serializer_class = serializers.AudioModelSerializer
    

class VideoCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAdmin]
    queryset = models.VideoModel.objects.all()
    serializer_class = serializers.VideoModelSerializer


class VideoGpdView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdmin]
    queryset = models.VideoModel.objects.all()
    serializer_class = serializers.VideoModelSerializer


class ImageCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAdmin]
    queryset = models.ImageModel.objects.all()
    serializer_class = serializers.ImageModelSerializer


class ImageGpdView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdmin]
    queryset = models.ImageModel.objects.all()
    serializer_class = serializers.ImageModelSerializer


class SliderVideoCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAdmin]
    serializer_class = serializers.SliderVideoListSerializer


class SliderVideoListAPIView(generics.ListAPIView):
    serializer_class = serializers.SliderVideoListSerializer
    queryset = models.SliderVideoModel.objects.all()
    

class EventByNewAPIView(generics.ListAPIView):
    serializer_class = serializers.EventModelSerializer
    queryset = models.EventModel.objects.order_by('date')
    

class EventByViewsAPIView(generics.ListAPIView):
    serializer_class = serializers.EventModelSerializer
    queryset = models.EventModel.objects.annotate(
        view_count=models.Subquery(
            models.ViewCount.objects.filter(event=models.OuterRef('pk')).values('count')[:1]
        )
    ).order_by('view_count')
    

class EventByWeekAPIView(generics.ListAPIView):
    serializer_class = serializers.EventModelSerializer
    queryset = models.EventModel.objects.filter(title="weekly event")
    

class EventByEventsAPIView(generics.ListAPIView):
    serializer_class = serializers.EventModelSerializer
    queryset = models.EventModel.objects.filter(title__startswith=("night of"))
    
    

class EventByYearMonthAPIView(generics.ListAPIView):
    serializer_class = serializers.EventModelSerializer

    def get_queryset(self):
        year = self.request.query_params.get('year')
        month = self.request.query_params.get('month')
        queryset = models.EventModel.objects.filter(
            Q(date__year=year, date__month=month)).order_by('date')
        return queryset


class SearchAPIView(generics.ListAPIView):
    queryset = models.EventModel.objects.all()
    serializer_class = serializers.EventModelSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'date']
    

class SliderRetrieveAPIView(APIView):

    def get(self, request):
        queryset = models.Slider.objects.all()
        serializer = serializers.SliderSerializer(instance=queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    


class RecentEventsAPIView(generics.ListAPIView):
    serializer_class = serializers.EventModelSerializer
    two_months_ago = date.today() - timedelta(days=60)
    queryset = models.EventModel.objects.filter(date__gte=two_months_ago)


class FutureEventsAPIView(generics.ListAPIView):
    serializer_class = serializers.EventModelSerializer
    future = date.today() + timedelta(days=60)
    queryset = models.EventModel.objects.filter(Q(date__lt=future, date__gte=date.today()))
    
    
class AudioByViewsAPIView(generics.ListAPIView):
    serializer_class = serializers.AudioModelSerializer
    queryset = models.AudioModel.objects.annotate(
        view_count=models.Subquery(
            models.ViewCount.objects.filter(event=models.OuterRef('pk')).values('count')[:1]
        )
    ).order_by('view_count')
    

class VideoByViewsAPIView(generics.ListAPIView):
    serializer_class = serializers.VideoModelSerializer
    queryset = models.VideoModel.objects.annotate(
        view_count=models.Subquery(
            models.ViewCount.objects.filter(event=models.OuterRef('pk')).values('count')[:1]
        )
    ).order_by('view_count')
    
    
class LikeAudioAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, audio_id):
        audio = models.AudioModel.objects.get(id=audio_id)
        liked_audio, created = models.LikedAudio.objects.get_or_create(user=request.user, audio=audio)
        if not created:
            return Response({'message': 'Audio already liked'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = serializers.LikedAudioSerializer(liked_audio)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
