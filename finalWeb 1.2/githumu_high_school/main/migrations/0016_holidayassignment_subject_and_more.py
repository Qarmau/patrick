# Generated by Django 5.0.7 on 2024-08-15 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_holidayassignment_grade_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='holidayassignment',
            name='subject',
            field=models.CharField(default='MATH', max_length=100),
        ),
        migrations.AlterField(
            model_name='holidayassignment',
            name='title',
            field=models.CharField(choices=[('May Holiday', 'May Holiday'), ('August Holiday', 'August Holiday'), ('December Holiday', 'December Holiday')], max_length=200),
        ),
    ]
