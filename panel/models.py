from django.db import models
from django.db.models import OuterRef, Subquery
from users.models import UsersRegister


class Slider(models.Model):
    image = models.ImageField()
    text = models.TextField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.text}"
    

class EventModel(models.Model):
    image = models.ImageField()
    title = models.TextField()
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.title}"    


class AudioModel(models.Model):
    event_model = models.ForeignKey(EventModel, on_delete=models.CASCADE)
    title = models.TextField()
    text = models.TextField()
    audio = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.text}"


class VideoModel(models.Model):
    event_model = models.ForeignKey(EventModel, on_delete=models.CASCADE)
    title = models.TextField()
    text = models.TextField()
    video = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.text}"
    
    
class ImageModel(models.Model):
    event_model = models.ForeignKey(EventModel, on_delete=models.CASCADE)
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)


class ViewCount(models.Model):
    event = models.OneToOneField(EventModel, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.event.title}: {self.count} views"


class SliderVideoModel(models.Model):
    title = models.TextField()
    text = models.TextField()
    video = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}"
    

class AudioCount(models.Model):
    audio = models.OneToOneField(AudioModel, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.audio.title}: {self.count} views"
    

class VideoCount(models.Model):
    video = models.OneToOneField(VideoModel, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.video.title}: {self.count} views"
    

class LikedAudio(models.Model):
    user = models.ForeignKey(UsersRegister, on_delete=models.CASCADE)
    audio = models.ForeignKey(AudioModel, on_delete=models.CASCADE)
    liked_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.user} liked {self.audio}"
    
