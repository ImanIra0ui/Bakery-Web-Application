# Generated by Django 3.1.3 on 2021-01-19 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingcart', '0016_auto_20210110_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='Orders',
            field=models.ManyToManyField(to='shoppingcart.Order'),
        ),
    ]