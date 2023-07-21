# Generated by Django 4.2.2 on 2023-06-26 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StudentName', models.CharField(max_length=255)),
                ('Address', models.TextField()),
                ('Age', models.IntegerField()),
                ('EmailID', models.EmailField(max_length=254)),
                ('JoiningDate', models.DateField()),
                ('Qualification', models.CharField(max_length=255)),
                ('Gender', models.CharField(max_length=255)),
                ('MobileNumber', models.CharField(max_length=255)),
            ],
        ),
    ]