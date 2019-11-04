# Generated by Django 2.2.3 on 2019-10-31 09:55

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sistema',
            fields=[
                ('id_system', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('bd_name', models.CharField(max_length=200)),
                ('bd_password', models.CharField(max_length=200)),
                ('bd_username', models.CharField(max_length=200)),
                ('bd_type', models.CharField(choices=[('mysql', 'Mysql'), ('postgresql', 'PostgreSQL')], max_length=11)),
                ('frequency', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('type_frequency', models.CharField(choices=[('days', 'Days'), ('hours', 'Hours'), ('minutes', 'Minutes'), ('seconds', 'Seconds')], max_length=11)),
                ('server_ip', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(re.compile('([0-9]{1,3}.?){4}'), 'ip incorrecta', 'invalid')])),
                ('server_username', models.CharField(max_length=200)),
                ('server_password', models.CharField(max_length=200)),
                ('server_route_save', models.CharField(blank=True, max_length=500, null=True)),
                ('receptor_server_username', models.CharField(blank=True, max_length=200, null=True)),
                ('receptor_server_ip', models.CharField(blank=True, max_length=20, null=True, validators=[django.core.validators.RegexValidator(re.compile('([0-9]{1,3}.?){4}'), 'ip incorrecta', 'invalid')])),
                ('receptor_route_save', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
