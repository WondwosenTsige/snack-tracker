# Generated by Django 3.2.6 on 2021-08-26 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snacks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snack',
            name='description',
            field=models.TextField(default=0, max_length=100),
        ),
    ]