# Generated by Django 2.0.2 on 2018-07-20 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='steps',
            name='step_no',
        ),
    ]
