# Generated by Django 4.2.1 on 2023-05-28 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DiseasesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Age', models.FloatField(default=0)),
                ('Gender', models.CharField(max_length=100)),
                ('Ethnicity', models.CharField(max_length=100)),
                ('jaundice', models.BooleanField()),
                ('A1', models.CharField(max_length=10)),
                ('A2', models.CharField(max_length=10)),
                ('A3', models.CharField(max_length=10)),
                ('A4', models.CharField(max_length=10)),
                ('A5', models.CharField(max_length=10)),
                ('A6', models.CharField(max_length=10)),
                ('A7', models.CharField(max_length=10)),
                ('A8', models.CharField(max_length=10)),
            ],
        ),
    ]