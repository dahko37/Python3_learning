# Generated by Django 3.0.4 on 2020-04-02 13:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_auto_20200402_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversation',
            name='creation_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date of creation'),
        ),
    ]
