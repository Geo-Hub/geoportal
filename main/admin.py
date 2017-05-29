from django.contrib import admin
from models import OwnershipInfo, IdentifiedNew, Shamba,MonthlyWeatherByCity
from leaflet.admin import LeafletGeoAdmin

# Register your models here.
class ShambaAdmin(admin.ModelAdmin):
	fields = ('balance','objectid_1','objectid','shape_leng','perimeter','parcel_no','shamba_owner','soil_type','state','cost_value','pic_url','electricit','water','outlinetra',
		'shape_le_1','shape_area','geom')
	list_display = ['balance','objectid_1','objectid','shape_leng','perimeter','parcel_no','shamba_owner','soil_type','state','cost_value','pic_url','electricit','water']
	class Meta:
		ordering = ('balance',)


admin.site.register(OwnershipInfo)
admin.site.register(IdentifiedNew,LeafletGeoAdmin)
admin.site.register(Shamba,ShambaAdmin)
admin.site.register(MonthlyWeatherByCity)