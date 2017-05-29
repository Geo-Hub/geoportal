# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_paymentinfo_paid_for'),
    ]

    operations = [
        migrations.AddField(
            model_name='shamba',
            name='balance',
            field=models.IntegerField(null=True),
        ),
    ]
