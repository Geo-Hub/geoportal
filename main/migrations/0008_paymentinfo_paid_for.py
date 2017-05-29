# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20151122_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentinfo',
            name='paid_for',
            field=models.ForeignKey(to='main.OwnershipInfo', null=True),
        ),
    ]
