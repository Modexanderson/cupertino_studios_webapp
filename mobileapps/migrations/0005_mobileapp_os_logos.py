# Generated by Django 4.2.6 on 2023-10-10 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobileapps', '0004_remove_mobileapp_screenshots_delete_screenshot_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobileapp',
            name='os_logos',
            field=models.JSONField(default=dict),
        ),
    ]
