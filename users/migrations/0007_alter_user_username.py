# Generated by Django 5.0.3 on 2024-04-09 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_email_alter_user_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=40, null=True, unique=True, verbose_name='Никнейм'),
        ),
    ]