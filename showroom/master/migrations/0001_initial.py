# Generated by Django 3.2 on 2021-07-22 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Vehicle_Name', models.CharField(max_length=100)),
                ('Vehicle_Type', models.CharField(max_length=100)),
                ('Description', models.TextField(max_length=300)),
                ('Vehicle_Color', models.CharField(max_length=100)),
                ('Rate', models.IntegerField()),
                ('TRate', models.IntegerField(default=100)),
                ('Weight', models.CharField(max_length=100)),
                ('Capacity', models.CharField(max_length=100)),
                ('Mileage', models.CharField(max_length=100)),
                ('Fuel', models.CharField(max_length=100)),
                ('Vehicle_Model', models.CharField(max_length=100)),
                ('Year_of_built', models.CharField(max_length=100)),
                ('Autogear', models.CharField(max_length=100)),
                ('Seatcap', models.CharField(max_length=100)),
                ('Center_lock', models.CharField(max_length=100)),
                ('Power_steering', models.CharField(max_length=100)),
                ('Power_break', models.CharField(max_length=100)),
                ('Tyre', models.CharField(max_length=100)),
                ('Chassis', models.CharField(max_length=100)),
                ('Vehicle_Image', models.ImageField(upload_to='media/images')),
            ],
        ),
        migrations.CreateModel(
            name='Accessories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Accessory_Name', models.CharField(max_length=100)),
                ('Description', models.TextField(max_length=300)),
                ('Rate', models.IntegerField()),
                ('TRate', models.IntegerField(default=100)),
                ('Accessory_Image', models.ImageField(upload_to='media/images')),
                ('Vehicle_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.vehicle')),
            ],
        ),
    ]