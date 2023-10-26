# Generated by Django 3.2 on 2023-10-24 17:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_test_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 26, 17, 37, 11, 519894, tzinfo=utc), verbose_name='tugatish sanasi'),
        ),
        migrations.AlterField(
            model_name='test',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
