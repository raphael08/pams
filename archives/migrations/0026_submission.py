# Generated by Django 3.2 on 2023-03-08 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('archives', '0025_auto_20230225_1911'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('status', models.CharField(blank=True, choices=[('Reached', 'Reached'), ('Not Reached', 'Not Reached')], default='Not Reached', max_length=50, null=True)),
                ('level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='archives.level')),
            ],
        ),
    ]
