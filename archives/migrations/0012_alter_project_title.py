# Generated by Django 3.2 on 2023-06-12 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archives', '0011_rename_departmenet_submission_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
