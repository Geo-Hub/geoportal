# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_ownershipinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='shamba',
            name='shamba_owner',
            field=models.ForeignKey(to='main.OwnershipInfo', null=True),
        ),
    ]
