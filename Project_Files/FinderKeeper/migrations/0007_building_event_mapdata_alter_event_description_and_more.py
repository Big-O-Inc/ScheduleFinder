# Generated by Django 4.2.5 on 2023-11-27 03:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('FinderKeeper', '0006_alter_event_day'),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bldg', models.CharField(max_length=50)),
                ('link', models.URLField()),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='mapData',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='endTime',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='startTime',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
