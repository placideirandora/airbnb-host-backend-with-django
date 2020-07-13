from django.contrib import admin
from .models import PlaceInfo, PropertyAndGuestInfo, LocationInfo

# Register your models here.
admin.site.register(PlaceInfo)
admin.site.register(PropertyAndGuestInfo)
admin.site.register(LocationInfo)
