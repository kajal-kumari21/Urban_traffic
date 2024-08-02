# Generated by Django 5.0.7 on 2024-07-13 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='trafficData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=255)),
                ('timestamp', models.DateTimeField()),
                ('vehicle_count', models.IntegerField()),
                ('average_speed', models.FloatField()),
            ],
        ),
    ]