# Generated by Django 4.0.5 on 2022-08-06 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0007_user_is_headhunter_user_is_looking_job_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_headhunter',
            field=models.BooleanField(choices=[('Yes', True), ('No', False)], default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_looking_job',
            field=models.BooleanField(choices=[('Yes', True), ('No', False)], default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_student',
            field=models.BooleanField(choices=[('Yes', True), ('No', False)], default=False),
        ),
    ]
