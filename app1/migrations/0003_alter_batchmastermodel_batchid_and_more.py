# Generated by Django 5.0.7 on 2024-07-12 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_coursemaster_exammaster_papermaster_semmaster_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batchmastermodel',
            name='batchid',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='batchmastermodel',
            name='batchno',
            field=models.IntegerField(default=0),
        ),
    ]
