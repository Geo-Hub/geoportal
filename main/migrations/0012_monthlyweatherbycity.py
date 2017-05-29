# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20151123_2123'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonthlyWeatherByCity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('month', models.IntegerField()),
                ('boston_temp', models.DecimalField(max_digits=5, decimal_places=1)),
                ('houston_temp', models.DecimalField(max_digits=5, decimal_places=1)),
            ],
        ),
    ]
