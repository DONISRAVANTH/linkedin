# Generated by Django 5.0.1 on 2024-02-09 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobseeker', '0012_notification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobapplication',
            name='hired',
        ),
        migrations.DeleteModel(
            name='Notification',
        ),
    ]
