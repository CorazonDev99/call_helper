# Generated by Django 5.0.3 on 2024-04-01 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('breaks', '0009_rename_breaktstatus_breakstatus_break'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='break',
            options={'ordering': ['-replacement__date', 'break_start'], 'verbose_name': 'Обеденный перерыв', 'verbose_name_plural': 'Обеденный перерывы'},
        ),
    ]
