# Generated by Django 4.0.2 on 2022-03-15 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('updates', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='refueling',
            name='price_p',
            field=models.IntegerField(default=1),
        ),
    ]
