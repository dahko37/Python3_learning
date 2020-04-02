# Generated by Django 3.0.4 on 2020-04-02 10:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conversation_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='author',
            field=models.CharField(default='Anonimous', max_length=20),
        ),
        migrations.AddField(
            model_name='message',
            name='conversation',
            field=models.CharField(default='Void', max_length=50),
        ),
        migrations.AlterField(
            model_name='message',
            name='send_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date sent'),
        ),
    ]
