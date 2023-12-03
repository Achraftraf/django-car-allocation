# Generated by Django 4.2.7 on 2023-12-03 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allocation',
            fields=[
                ('allocation_id', models.AutoField(primary_key=True, serialize=False)),
                ('allocation_date', models.DateField()),
                ('allocation_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('allocation_nbr_days', models.IntegerField()),
                ('client_id', models.IntegerField()),
                ('car_id', models.IntegerField()),
            ],
            options={
                'db_table': 'allocation',
            },
        ),
    ]