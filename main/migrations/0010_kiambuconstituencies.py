# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_shamba_balance'),
    ]

    operations = [
        migrations.CreateModel(
            name='KiambuConstituencies',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('objectid', models.IntegerField()),
                ('const_nam', models.CharField(max_length=50)),
                ('shape_leng', models.FloatField()),
                ('shape_area', models.FloatField()),
                ('population', models.IntegerField()),
                ('pop_densty', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
            ],
        ),
    ]
