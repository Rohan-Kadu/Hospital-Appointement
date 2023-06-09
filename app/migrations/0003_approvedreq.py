# Generated by Django 4.0.3 on 2022-04-01 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_admindb_alter_userrequest_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='approvedReq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AppointementId', models.BigIntegerField()),
                ('Firstname', models.CharField(max_length=50)),
                ('Lastname', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=50)),
                ('Address', models.TextField(max_length=50)),
                ('Gender', models.CharField(max_length=50)),
                ('Contact', models.BigIntegerField()),
                ('Date', models.DateField()),
                ('Time', models.TimeField()),
                ('SelectDoctor', models.CharField(max_length=50)),
                ('Comment', models.CharField(max_length=50)),
            ],
        ),
    ]
