# Generated by Django 4.2.6 on 2023-10-10 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobileapps', '0003_remove_screenshot_app'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mobileapp',
            name='screenshots',
        ),
        migrations.DeleteModel(
            name='Screenshot',
        ),
        migrations.AddField(
            model_name='mobileapp',
            name='screenshots',
            field=models.TextField(blank=True, help_text='Enter screenshot URLs separated by newlines'),
        ),
    ]
