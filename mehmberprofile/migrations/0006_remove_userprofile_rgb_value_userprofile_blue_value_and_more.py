# Generated by Django 4.2 on 2023-04-10 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mehmberprofile', '0005_remove_membershiphistory_amount_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='rgb_value',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='blue_value',
            field=models.CharField(default='0', max_length=7),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='green_value',
            field=models.CharField(default='0', max_length=7),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='red_value',
            field=models.CharField(default='0', max_length=7),
        ),
    ]
