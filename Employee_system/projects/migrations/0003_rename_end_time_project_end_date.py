# Generated by Django 5.0.4 on 2024-04-20 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_rename_fullname_project_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='end_time',
            new_name='end_date',
        ),
    ]