# Generated by Django 5.0.1 on 2024-02-05 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobseeker', '0002_alter_jobapplication_resume'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobseeker',
            name='resume',
            field=models.FileField(null=True, upload_to='resume/'),
        ),
    ]
