# -*- coding: utf-8 -*-
# Generated by Victor on 2023-05-14

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0001_initial')
    ]
    operations = [
        migrations.RemoveField('KiambuCounty', 'varname_2'),
        migrations.RemoveField('KiambuCounty', 'nl_name_2'),
        migrations.RemoveField('KiambuCounty', 'cc_2'),
    ]