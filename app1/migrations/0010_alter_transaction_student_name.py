# Generated by Django 5.0.7 on 2024-07-13 06:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_alter_transaction_student_reg_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='student_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app1.studentmaster'),
        ),
    ]
