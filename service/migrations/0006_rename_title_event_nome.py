# Generated by Django 5.0 on 2024-10-25 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_rename_name_event_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='title',
            new_name='nome',
        ),
    ]
