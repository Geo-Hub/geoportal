from django.conf import settings
from django.contrib.gis.db import models

# Create your models here.


class Registration(models.Model):
    id = models.AutoField(primary_key=True)
    submitted_from = models.CharField(max_length=50, null=False)
    parcel_no = models.CharField(max_length=20, null=False)
    date_submitted = models.DateTimeField(auto_now_add=True, null=False)

    def __unicode__(self):
        return self.submitted_from


class ContactMessage(models.Model):
    id = models.AutoField(primary_key=True)
    name_of_sender = models.CharField(max_length=50, null=False)
    email_address = models.EmailField(max_length=254, null=False)
    message = models.TextField(max_length=200, null=False)


class OwnershipInfoManager(models.Manager):
    def get_current_user(self, owner):
        return super(OwnershipInfoManager, self).filter(user=owner)


class OwnershipInfo(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=True)
    id_number = models.IntegerField()
    balance = models.IntegerField()

    objects = OwnershipInfoManager()


class RatesPayable(models.Model):
    id = models.AutoField(primary_key=True)
    pass


class PaymentInfo(models.Model):
    id = models.AutoField(primary_key=True)
    amount = models.IntegerField()
    receipt_number = models.IntegerField()
    date_of_payment = models.DateField()
    paid_by = models.CharField(max_length=50)
    paid_for = models.ForeignKey(OwnershipInfo, on_delete=models.CASCADE, null=True)


class Shamba(models.Model):
    LEASE_CHOICES = (
        ("Freehold", "Free-hold"),
        ("Leasehold", "Leasehold"),
    )
    ZONE_CHOICES = (
        ("Industrial", "Industrial"),
        ("Commercial", "Commercial"),
        ("Residential", "Residential"),
    )
    LAND_USE_CHOICES = (
        ("Agricultural", "Agricultural"),
        ("Bare_Land", "Bare_Land"),
    )
    id = models.AutoField(primary_key=True)
    shamba_owner = models.ForeignKey(OwnershipInfo, on_delete=models.CASCADE, null=True)
    balance = models.IntegerField(null=True)
    objectid_1 = models.IntegerField()
    objectid = models.IntegerField()
    shape_leng = models.FloatField()
    y_coordina = models.IntegerField()
    x_coordina = models.IntegerField()
    perimeter = models.IntegerField()
    parcel_no = models.IntegerField()
    owner = models.CharField(max_length=254)
    soil_type = models.CharField(max_length=254)
    state = models.CharField(max_length=254)
    cost_value = models.IntegerField()
    pic_url = models.CharField(max_length=254, null=True)
    electricit = models.CharField(max_length=254, null=True)
    water = models.CharField(max_length=254, null=True)
    outlinetra = models.FloatField()
    shape_le_1 = models.FloatField()
    shape_area = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    type_of_lease = models.CharField(max_length=20, choices=LEASE_CHOICES, null=True)
    zone = models.CharField(max_length=20, choices=ZONE_CHOICES, null=True)
    period_of_lease = models.IntegerField(null=True)
    land_use = models.CharField(max_length=20, choices=LAND_USE_CHOICES, null=True)
    objects = models.Manager()

    def __str__(self):
        return str(self.parcel_no)


class LandOwner(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=200)
    second_name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    id_number = models.IntegerField()
    land = models.ForeignKey(Shamba, on_delete=models.CASCADE)


class IdentifiedNew(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70, null=True)
    general_location = models.CharField(max_length=70, null=True)
    geom = models.MultiPolygonField(srid=4326)
    objects = models.Manager()


class KiambuCounty(models.Model):
    id_0 = models.IntegerField(primary_key=True)
    iso = models.CharField(max_length=254)
    name_0 = models.CharField(max_length=254)
    id_1 = models.IntegerField()
    name_1 = models.CharField(max_length=254)
    id_2 = models.IntegerField()
    name_2 = models.CharField(max_length=254)
    hasc_2 = models.CharField(max_length=254)
    type_2 = models.CharField(max_length=254)
    engtype_2 = models.CharField(max_length=254)
    validfr_2 = models.CharField(max_length=254)
    validto_2 = models.CharField(max_length=254)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.PolygonField(srid=4326)
    objects = models.Manager()

    def __str__(self):
        return self.name_2

    class Meta:
        verbose_name_plural = "Kiambu County"


class KiambuDivision(models.Model):
    id_0 = models.IntegerField(primary_key=True)
    iso = models.CharField(max_length=254)
    name_0 = models.CharField(max_length=254)
    id_1 = models.IntegerField()
    name_1 = models.CharField(max_length=254)
    id_2 = models.IntegerField()
    name_2 = models.CharField(max_length=254)
    id_3 = models.IntegerField()
    name_3 = models.CharField(max_length=254)
    varname_3 = models.CharField(max_length=254)
    nl_name_3 = models.CharField(max_length=254)
    hasc_3 = models.CharField(max_length=254)
    type_3 = models.CharField(max_length=254)
    engtype_3 = models.CharField(max_length=254)
    validfr_3 = models.CharField(max_length=254)
    validto_3 = models.CharField(max_length=254)
    remarks_3 = models.CharField(max_length=254)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.PolygonField(srid=4326)
    objects = models.Manager()


class KiambuLocation(models.Model):
    id_0 = models.IntegerField(primary_key=True)
    iso = models.CharField(max_length=254)
    name_0 = models.CharField(max_length=254)
    id_1 = models.IntegerField()
    name_1 = models.CharField(max_length=254)
    id_2 = models.IntegerField()
    name_2 = models.CharField(max_length=254)
    id_3 = models.IntegerField()
    name_3 = models.CharField(max_length=254)
    id_4 = models.IntegerField()
    name_4 = models.CharField(max_length=254)
    varname_4 = models.CharField(max_length=254)
    type_4 = models.CharField(max_length=254)
    engtype_4 = models.CharField(max_length=254)
    validfr_4 = models.CharField(max_length=254)
    validto_4 = models.CharField(max_length=254)
    remarks_4 = models.CharField(max_length=254)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    objects = models.Manager()


class KiambuSublocation(models.Model):
    id_0 = models.IntegerField(primary_key=True)
    iso = models.CharField(max_length=254)
    name_0 = models.CharField(max_length=254)
    id_1 = models.IntegerField()
    name_1 = models.CharField(max_length=254)
    id_2 = models.IntegerField()
    name_2 = models.CharField(max_length=254)
    id_3 = models.IntegerField()
    name_3 = models.CharField(max_length=254)
    id_4 = models.IntegerField()
    name_4 = models.CharField(max_length=254)
    id_5 = models.IntegerField()
    name_5 = models.CharField(max_length=254)
    type_5 = models.CharField(max_length=254)
    engtype_5 = models.CharField(max_length=254)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.PolygonField(srid=4326)
    objects = models.Manager()


class KiambuConstituencies(models.Model):
    objectid = models.IntegerField(primary_key=True)
    const_nam = models.CharField(max_length=50)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    population = models.IntegerField(null=True)
    pop_densty = models.IntegerField(null=True)
    geom = models.MultiPolygonField(srid=4326)
    objects = models.Manager()


class MonthlyWeatherByCity(models.Model):
    id = models.AutoField(primary_key=True)
    month = models.IntegerField()
    boston_temp = models.DecimalField(max_digits=5, decimal_places=1)
    houston_temp = models.DecimalField(max_digits=5, decimal_places=1)
