# Generated by Django 4.2.14 on 2024-07-31 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tips', '0006_alter_feedback_options_alter_gardentip_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gardentip',
            name='season',
            field=models.CharField(choices=[('Spring', 'SPRING'), ('Summer', 'SUMMER'), ('Autumn', 'AUTUMN'), ('Winter', 'WINTER')], default='summer'),
        ),
    ]
