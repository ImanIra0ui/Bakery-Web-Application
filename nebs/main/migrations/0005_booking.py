# Generated by Django 3.1.3 on 2020-12-19 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20201207_1448'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=100)),
                ('day', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
            ],
        ),
    ]
