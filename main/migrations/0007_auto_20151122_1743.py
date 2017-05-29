# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_shamba_shamba_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='IdentifiedNew',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=70, null=True)),
                ('general_location', models.CharField(max_length=70, null=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.IntegerField()),
                ('receipt_number', models.IntegerField()),
                ('date_of_payment', models.DateField()),
                ('paid_by', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='RatesPayable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.AddField(
            model_name='ownershipinfo',
            name='first_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
