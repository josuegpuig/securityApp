# Generated by Django 3.0.4 on 2020-03-11 01:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('evaluations', '0003_evaluation_classification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluation',
            name='classification',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='user',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, related_name='evaluations', to=settings.AUTH_USER_MODEL),
        ),
    ]
