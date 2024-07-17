# Generated by Django 5.0.6 on 2024-07-14 01:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_alter_studentmaster_batchno_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmaster',
            name='batchno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.batchmaster'),
        ),
        migrations.AlterField(
            model_name='studentmaster',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.coursemaster'),
        ),
        migrations.AlterField(
            model_name='studentmaster',
            name='sem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.semmaster'),
        ),
    ]
