# Generated by Django 3.0.4 on 2020-03-10 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0005_auto_20200310_0642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='short_name',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
