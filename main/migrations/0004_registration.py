# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_contactmessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('submitted_from', models.CharField(max_length=50)),
                ('parcel_no', models.CharField(max_length=20)),
                ('date_submitted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
