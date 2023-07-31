# Generated by Django 4.2.3 on 2023-07-31 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_weight', models.IntegerField()),
                ('max_capacity', models.IntegerField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('weight', models.IntegerField()),
                ('capacity', models.IntegerField()),
                ('status', models.BooleanField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('end_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='end_location', to='transport.location')),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transport.flight')),
                ('start_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='start_location', to='transport.location')),
            ],
        ),
    ]
