# Generated by Django 3.2.7 on 2021-09-16 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.TextField(max_length=20, null=True),
        ),
    ]