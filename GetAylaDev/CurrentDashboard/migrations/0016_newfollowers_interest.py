# Generated by Django 3.1.1 on 2021-07-16 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CurrentDashboard', '0015_remove_newfollowers_interest'),
    ]

    operations = [
        migrations.AddField(
            model_name='newfollowers',
            name='interest',
            field=models.CharField(default='NULL', max_length=200),
        ),
    ]