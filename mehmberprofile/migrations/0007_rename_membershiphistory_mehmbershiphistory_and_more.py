# Generated by Django 4.2 on 2023-04-10 20:55

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mehmberprofile', '0006_remove_userprofile_rgb_value_userprofile_blue_value_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MembershipHistory',
            new_name='MehmbershipHistory',
        ),
        migrations.AlterModelOptions(
            name='mehmbershiphistory',
            options={'verbose_name_plural': 'Mehmbership Histories'},
        ),
        migrations.AlterModelOptions(
            name='paymenthistory',
            options={'verbose_name_plural': 'Payment Histories'},
        ),
    ]