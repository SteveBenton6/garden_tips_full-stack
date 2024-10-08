# Generated by Django 4.2.14 on 2024-07-31 11:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tips', '0004_alter_gardentip_region_alter_gardentip_season'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tip_feedback', models.TextField()),
                ('score', models.IntegerField(choices=[(1, '*'), (2, '**'), (3, '***'), (4, '****'), (5, '*****')], default=3)),
                ('approved', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='respondent', to=settings.AUTH_USER_MODEL)),
                ('garden_tip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedback', to='tips.gardentip')),
            ],
        ),
    ]
