# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_monthlyweatherbycity'),
    ]

    operations = [
        migrations.AddField(
            model_name='shamba',
            name='land_use',
            field=models.CharField(max_length=20, null=True, choices=[(b'Agricultural', b'Agricultural'), (b'Bare_Land', b'Bare_Land')]),
        ),
        migrations.AddField(
            model_name='shamba',
            name='period_of_lease',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='shamba',
            name='type_of_lease',
            field=models.CharField(max_length=20, null=True, choices=[(b'Freehold', b'Free-hold'), (b'Leasehold', b'Leasehold')]),
        ),
        migrations.AddField(
            model_name='shamba',
            name='zone',
            field=models.CharField(max_length=20, null=True, choices=[(b'Industrial', b'Industrial'), (b'Commercial', b'Commercial'), (b'Residential', b'Residential')]),
        ),
    ]
