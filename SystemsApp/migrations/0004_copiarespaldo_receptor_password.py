# Generated by Django 2.2.3 on 2019-11-03 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SystemsApp', '0003_auto_20191102_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='copiarespaldo',
            name='receptor_password',
            field=models.CharField(default='password', max_length=200),
        ),
    ]