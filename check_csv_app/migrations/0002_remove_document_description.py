# Generated by Django 2.2.3 on 2019-07-22 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('check_csv_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='description',
        ),
    ]
