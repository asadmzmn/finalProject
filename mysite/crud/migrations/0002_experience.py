# Generated by Django 4.0.2 on 2022-03-07 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.CharField(max_length=1000)),
                ('post', models.CharField(max_length=1000)),
                ('experience', models.CharField(max_length=1000)),
                ('address', models.CharField(max_length=1000)),
            ],
        ),
    ]