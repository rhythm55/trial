# Generated by Django 2.0.2 on 2018-07-31 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faqs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='level',
            field=models.CharField(default='easy', max_length=20),
            preserve_default=False,
        ),
    ]
