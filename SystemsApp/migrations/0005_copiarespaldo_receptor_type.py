# Generated by Django 2.2.3 on 2019-11-05 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SystemsApp', '0004_copiarespaldo_receptor_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='copiarespaldo',
            name='receptor_type',
            field=models.CharField(choices=[('drive', 'Drive'), ('server', 'Server')], default='server', max_length=11),
        ),
    ]
