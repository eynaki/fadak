from django.contrib import admin
from . import models


admin.site.register(models.Slider)
admin.site.register(models.EventModel)
admin.site.register(models.AudioModel)
admin.site.register(models.VideoModel)
admin.site.register(models.ImageModel)
admin.site.register(models.ViewCount)
admin.site.register(models.SliderVideoModel)
admin.site.register(models.AudioCount)
admin.site.register(models.VideoCount)
admin.site.register(models.LikedAudio)
