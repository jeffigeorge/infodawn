# Generated by Django 3.2 on 2021-07-22 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='breakdown',
            name='Status',
            field=models.CharField(default='Our Customer care executive will call you soon', max_length=200),
        ),
    ]
