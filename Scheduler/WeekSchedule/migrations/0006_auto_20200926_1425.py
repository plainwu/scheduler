# Generated by Django 3.0.8 on 2020-09-26 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WeekSchedule', '0005_auto_20200925_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='status',
            field=models.TextField(choices=[('Done', 'Done'), ('1/3 left', '1/3 left'), ('Just started', 'Just started'), ('Failed', 'Failed'), ('Waiting', 'Waiting')], default='Waiting'),
        ),
    ]