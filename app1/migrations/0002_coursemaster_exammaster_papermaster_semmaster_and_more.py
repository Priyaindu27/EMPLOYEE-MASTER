# Generated by Django 5.0.7 on 2024-07-12 07:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=5)),
                ('courseid', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ExamMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('examid', models.IntegerField(default=0)),
                ('examtype', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='PaperMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('papername', models.CharField(max_length=60)),
                ('papercode', models.CharField(max_length=60)),
                ('papertype', models.CharField(max_length=60)),
                ('papersheetname', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='SemMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sem', models.CharField(max_length=4)),
                ('semid', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='batchmastermodel',
            name='batchno',
            field=models.CharField(max_length=20),
        ),
        migrations.CreateModel(
            name='StudentMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentname', models.CharField(max_length=60)),
                ('studentregno', models.IntegerField(default=0)),
                ('batchno', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app1.batchmastermodel')),
                ('course', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app1.coursemaster')),
                ('sem', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app1.semmaster')),
            ],
        ),
    ]
