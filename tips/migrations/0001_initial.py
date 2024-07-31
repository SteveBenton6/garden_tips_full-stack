# Generated by Django 4.2.14 on 2024-07-31 10:23

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GardenTips',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('season', models.IntegerField(choices=[('spring', 'SPRING'), ('summer', 'SUMMER'), ('autumn', 'AUTUMN'), ('winter', 'WINTER')], default=0)),
                ('region', models.IntegerField(choices=[('SE', 'SOUTHERN ENGLAND'), ('WE', 'WESTERN ENGLAND'), ('WA', 'WALES'), ('NE', 'NORTEHRN ENGLAND'), ('SC', 'SCOTLAND'), ('NI', 'NORTHERN IRELAND')], default=0)),
                ('image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('garden_tip', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tip_creator', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
