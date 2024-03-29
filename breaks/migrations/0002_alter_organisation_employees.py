# Generated by Django 5.0.3 on 2024-03-28 06:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('breaks', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisation',
            name='employees',
            field=models.ManyToManyField(blank=True, related_name='organisation_employees', to=settings.AUTH_USER_MODEL, verbose_name='Сотрудники'),
        ),
    ]
