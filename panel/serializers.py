from rest_framework import serializers

from . import models


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Slider
        fields = ["image", "text"]


class AudioModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AudioModel
        fields = ("__all__")


class VideoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VideoModel
        fields = ("__all__")


class ImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ImageModel
        fields = ("__all__")


class EventModelSerializer(serializers.ModelSerializer):
    audio = AudioModelSerializer(many=True, read_only=True)
    video = VideoModelSerializer(many=True, read_only=True)
    image2 = ImageModelSerializer(many=True, read_only=True)

    class Meta:
        model = models.EventModel
        fields = ("__all__")


class SliderVideoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SliderVideoModel
        fields = '__all__'
       
        
class LikedAudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LikedAudio
        fields = "__all__"
