# Generated by Django 4.0.3 on 2022-03-17 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=36, unique=True),
        ),
    ]