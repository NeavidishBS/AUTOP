# Generated by Django 4.0.2 on 2022-03-15 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('parking', '0001_initial'),
        ('fuel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classes', models.CharField(choices=[('Car', 'CAR'), ('Truck', 'TRUCK')], max_length=20)),
                ('brand', models.CharField(choices=[('BMW', 'BMW'), ('MERCEDES', 'Mercedes'), ('TOYOTA', 'Toyota'), ('HUNDAI', 'Hundai'), ('LADA', 'Lada')], max_length=20)),
                ('serie', models.CharField(max_length=100)),
                ('tonnage', models.IntegerField(default=None)),
                ('petrol_capacity', models.FloatField(default=None, verbose_name='Capacity')),
                ('gas_type', models.ForeignKey(max_length=20, on_delete=django.db.models.deletion.DO_NOTHING, to='fuel.fuel')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_index', models.CharField(default=None, max_length=15)),
                ('photos', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/')),
                ('vehicle_insurance_doc', models.FileField(blank=True, null=True, upload_to='insuranse_docs//%Y/%m/%d/')),
                ('date_added', models.DateField(default=None, verbose_name='Date (yyyy-mm-dd):')),
                ('start_milage', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True, verbose_name='KM at stock')),
                ('car', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='vehicle.car')),
                ('parking_place', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='parking.p_parking')),
            ],
        ),
    ]
