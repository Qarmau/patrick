# Generated by Django 5.0.7 on 2024-08-15 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_holidayassignment_subject_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='holidayassignment',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
