# Generated by Django 5.0.1 on 2024-02-08 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobseeker', '0006_remove_jobapplication_resume'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobseeker',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='jobseeker',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
