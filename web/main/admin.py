from django.contrib.gis import admin

from .models import (
    IdentifiedNew,
    KiambuConstituencies,
    KiambuCounty,
    KiambuDivision,
    KiambuLocation,
    KiambuSublocation,
    MonthlyWeatherByCity,
    OwnershipInfo,
    Shamba,
)


@admin.register(Shamba)
class ShambaAdmin(admin.ModelAdmin):
    list_display = (
        "parcel_no",
        "shamba_owner",
        "balance",
        "soil_type",
        "state",
        "cost_value",
        "electricit",
        "water",
    )
    ordering = ("-balance",)
    list_filter = ("parcel_no",)


@admin.register(KiambuConstituencies)
class KiambuConstituenciesAdmin(admin.ModelAdmin):
    list_display = ("const_nam", "population", "pop_densty")


@admin.register(KiambuDivision)
class KiambuDivisionAdmin(admin.ModelAdmin):
    pass


@admin.register(KiambuLocation)
class KiambuLocationAdmin(admin.ModelAdmin):
    pass


@admin.register(KiambuSublocation)
class KiambuSublocationAdmin(admin.ModelAdmin):
    pass


admin.site.register(OwnershipInfo)
admin.site.register(IdentifiedNew)
admin.site.register(MonthlyWeatherByCity)
