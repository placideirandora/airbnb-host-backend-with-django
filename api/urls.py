from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/v1/post-place-info',
         views.post_place_info, name='post-place-info'),
    path('api/v1/get-place-info',
         views.get_place_info, name='get-place-info'),
    path('api/v1/post-property-info',
         views.post_property_info, name='post-property-info'),
    path('api/v1/get-property-info',
         views.get_property_info, name='get-property-info'),
    path('api/v1/post-location-info',
         views.post_location_info, name='post-location-info'),
    path('api/v1/get-location-info',
         views.get_location_info, name='get-location-info'),
]
