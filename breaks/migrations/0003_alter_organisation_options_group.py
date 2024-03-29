# Generated by Django 5.0.3 on 2024-03-28 06:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('breaks', '0002_alter_organisation_employees'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='organisation',
            options={'ordering': ['name'], 'verbose_name': 'Организация', 'verbose_name_plural': 'Организации'},
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('min_active', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Минимальное количество активных сотрудников')),
                ('break_start', models.TimeField(blank=True, null=True, verbose_name='Начало обеда')),
                ('break_end', models.TimeField(blank=True, null=True, verbose_name='Конец обеда')),
                ('break_max_duration', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Максимальная длительность обеда')),
                ('employees', models.ManyToManyField(blank=True, related_name='group_employees', to=settings.AUTH_USER_MODEL, verbose_name='Сотрудники')),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='group_managers', to=settings.AUTH_USER_MODEL, verbose_name='Директор')),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='breaks.organisation', verbose_name='Организация')),
            ],
            options={
                'verbose_name': 'Группа',
                'verbose_name_plural': 'Группы',
                'ordering': ['name'],
            },
        ),
    ]
