# Generated by Django 3.1.1 on 2021-07-10 03:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CurrentDashboard', '0003_auto_20210709_2215'),
    ]

    operations = [
        migrations.RenameField(
            model_name='instaprofiles',
            old_name='Province',
            new_name='country',
        ),
    ]