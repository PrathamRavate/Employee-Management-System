# Generated by Django 5.0.4 on 2024-04-20 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='FullName',
            new_name='name',
        ),
    ]
