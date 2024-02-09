# Generated by Django 5.0.1 on 2024-02-08 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobseeker', '0009_remove_jobseeker_applied_jobs'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobseeker',
            name='Phone',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='jobseeker',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='jobseeker',
            name='github',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='jobseeker',
            name='instagram',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='jobseeker',
            name='profile',
            field=models.ImageField(blank=True, null=True, upload_to='profile/'),
        ),
        migrations.AddField(
            model_name='jobseeker',
            name='twitter',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='jobseeker',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
    ]
