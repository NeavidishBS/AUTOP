# Generated by Django 4.0.2 on 2022-02-02 01:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vehicle', '0001_initial'),
        ('fuel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='refueling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=None, verbose_name='Date (yyyy-mm-dd):')),
                ('refueling', models.BooleanField(default=None)),
                ('fuel', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='fuel.fuel')),
                ('u_vechicle', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='vehicle.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='milage_update',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=None, verbose_name='Date (yyyy-mm-dd):')),
                ('milage_total', models.DecimalField(decimal_places=2, default=None, max_digits=18, verbose_name='KM Total Distance')),
                ('u_vechicle', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='vehicle.vehicle')),
            ],
        ),
    ]