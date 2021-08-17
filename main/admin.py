from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from .models import Provider, ServiceArea


# Register your models here.
admin.site.register(Provider)
admin.site.register(ServiceArea, LeafletGeoAdmin)
