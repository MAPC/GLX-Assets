from asset.models import Asset
# from django.contrib import admin
from django.contrib.gis import admin

class AssetAdmin(admin.GeoModelAdmin):
    list_display = ('pk','title')

admin.site.register(Asset, AssetAdmin)