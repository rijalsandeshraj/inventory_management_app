# Generated by Django 3.1.7 on 2021-03-23 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_stockhistory'),
    ]

    operations = [
        migrations.DeleteModel(
            name='StockHistory',
        ),
    ]