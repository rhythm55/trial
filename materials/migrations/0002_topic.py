# Generated by Django 2.0.2 on 2018-07-18 06:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_name', models.CharField(max_length=100)),
                ('language_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materials.language')),
            ],
        ),
    ]