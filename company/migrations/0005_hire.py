# Generated by Django 5.0.1 on 2024-02-09 09:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_remove_jobposting_hr_name_alter_company_company_hr'),
        ('jobseeker', '0011_jobapplication_hired'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hired_on', models.DateTimeField(auto_now_add=True)),
                ('job_posting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.jobposting')),
                ('job_seeker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobseeker.jobseeker')),
            ],
        ),
    ]
