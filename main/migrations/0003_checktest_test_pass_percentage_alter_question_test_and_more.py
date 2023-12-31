# Generated by Django 4.2.6 on 2023-10-15 13:31

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_auto_20231013_1839'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('true_answers', models.PositiveIntegerField(default=0)),
                ('percentage', models.PositiveIntegerField(default=0)),
                ('is_passed', models.BooleanField(default=False)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='test',
            name='pass_percentage',
            field=models.PositiveIntegerField(default=60),
        ),
        migrations.AlterField(
            model_name='question',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='main.test', verbose_name='test'),
        ),
        migrations.AlterField(
            model_name='test',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 17, 13, 31, 33, 992638, tzinfo=datetime.timezone.utc), verbose_name='tugatish sanasi'),
        ),
        migrations.CreateModel(
            name='ChekQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('given_answer', models.CharField(max_length=2)),
                ('true_answer', models.CharField(max_length=2)),
                ('is_true', models.BooleanField(default=False)),
                ('checktest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.checktest')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.question')),
            ],
        ),
        migrations.AddField(
            model_name='checktest',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.test'),
        ),
    ]
