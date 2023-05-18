from django.urls import path
from . import views


urlpatterns = [
    path("slider_create/", views.SliderCreatView.as_view()),
    path("slider_delete/<int:pk>/", views.SliderDelView.as_view()),
    path("slider_retrieve/", views.SliderRetrieveView.as_view()),
    path('events_create/', views.EventCreateView.as_view()),
    path('events_gpd/<int:pk>/', views.EventGpdView.as_view()),
    path('audio_create/', views.AudioCreateView.as_view()),
    path('audio_gpd/<int:pk>/', views.AudioGpdView.as_view()),
    path('video_create/', views.VideoCreateView.as_view()),
    path('video_gpd/<int:pk>/', views.VideoGpdView.as_view()),
    path('image_create/', views.ImageCreateView.as_view()),
    path('image_gpd/<int:pk>/', views.ImageGpdView.as_view()),
    path("slider_videos_create/", views.SliderVideoCreateAPIView.as_view()),
    
    path('slider_videos/', views.SliderVideoListAPIView.as_view()),
    path('eventbynew/', views.EventByNewAPIView.as_view()),
    path('eventbyviews/', views.EventByViewsAPIView.as_view()),
    path('eventbyweek/', views.EventByWeekAPIView.as_view()),
    path('eventbyevents/', views.EventByEventsAPIView.as_view()),
    path('eventbyym/', views.EventByYearMonthAPIView.as_view()),
    path('search/', views.SearchAPIView.as_view()),
    path('like/<int:audio_id>/', views.LikeAudioAPIView.as_view()),

    path("home_slider_retrieve/", views.SliderRetrieveAPIView.as_view()),
    path("recentlyevents/", views.RecentEventsAPIView.as_view()),
    path("futureevents/", views.FutureEventsAPIView.as_view()),
    path('audiobyviews/', views.AudioByViewsAPIView.as_view()),
    path('videobyviews/', views.VideoByViewsAPIView.as_view()),
]