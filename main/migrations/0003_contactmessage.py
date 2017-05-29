# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20151122_1638'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_of_sender', models.CharField(max_length=50)),
                ('email_address', models.EmailField(max_length=254)),
                ('message', models.TextField(max_length=200)),
            ],
        ),
    ]
