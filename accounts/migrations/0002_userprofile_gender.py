# Generated by Django 3.0.4 on 2020-03-11 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='gender',
            field=models.IntegerField(default=3),
        ),
    ]
