# Generated by Django 3.0.6 on 2020-06-24 09:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_auto_20200624_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 24, 9, 41, 34, 835282, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(max_length=10),
        ),
    ]
