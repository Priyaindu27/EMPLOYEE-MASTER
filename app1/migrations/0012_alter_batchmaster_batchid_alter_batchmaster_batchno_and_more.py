# Generated by Django 5.0.6 on 2024-07-13 13:22

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_remove_transaction_paper_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batchmaster',
            name='batchid',
            field=models.CharField(choices=[(' ', 'Select_Batch'), ('2020-2022', '2020-2022'), ('2021-2023', '2021-2023'), ('2022-2024', '2022-2024'), ('2023-2025', '2023-2025'), ('2024-2025', '2024-2025'), ('2025-2027', '2025-2027'), ('2026-2028', '2026-2028'), ('2027-2029', '2027-2029'), ('2028-2030', '2028-2030')], default=' ', max_length=10),
        ),
        migrations.AlterField(
            model_name='batchmaster',
            name='batchno',
            field=models.CharField(max_length=3, validators=[django.core.validators.RegexValidator(message='Enter only integer.', regex='^[0-9]+$')]),
        ),
        migrations.AlterField(
            model_name='coursemaster',
            name='course',
            field=models.CharField(max_length=5, validators=[django.core.validators.RegexValidator(message='Only alphabetic characters are allowed.', regex='^[a-zA-Z]*$')]),
        ),
        migrations.AlterField(
            model_name='coursemaster',
            name='courseid',
            field=models.CharField(max_length=5, validators=[django.core.validators.RegexValidator(message='Enter only integer.', regex='^[0-9]+$')]),
        ),
        migrations.AlterField(
            model_name='exammaster',
            name='examid',
            field=models.CharField(max_length=6, validators=[django.core.validators.RegexValidator(message='Enter only integer.', regex='^[0-9]+$')]),
        ),
        migrations.AlterField(
            model_name='exammaster',
            name='examtype',
            field=models.CharField(choices=[(' ', 'select-ExamType'), ('Internal-I', 'Internal-I'), ('Internal-II', 'Internal-II'), ('External', 'External')], default=' ', max_length=15),
        ),
        migrations.AlterField(
            model_name='papermaster',
            name='papercode',
            field=models.CharField(max_length=8, validators=[django.core.validators.RegexValidator(message='Enter proper PaperCode.', regex='^[a-zA-Z0-9]+$')]),
        ),
        migrations.AlterField(
            model_name='papermaster',
            name='papername',
            field=models.CharField(max_length=25, validators=[django.core.validators.RegexValidator(message='Enter proper PaperCode.', regex='^[a-zA-Z0-9]+$')]),
        ),
        migrations.AlterField(
            model_name='papermaster',
            name='papersheetname',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='Only alphabetic characters are allowed.', regex='^[a-zA-Z]*$')]),
        ),
        migrations.AlterField(
            model_name='papermaster',
            name='papertype',
            field=models.CharField(choices=[(' ', 'select PaperType'), ('CompulFoundation', 'CompulFoundation'), ('Core', 'Core'), ('Generic Elective', 'Generic Elective'), ('lab', 'lab'), ('open Elective', 'open Elective'), ('compulsory', 'compulsory')], default=' ', max_length=20),
        ),
        migrations.AlterField(
            model_name='semmaster',
            name='sem',
            field=models.CharField(choices=[(' ', 'select_semister'), ('First', 'First'), ('Second', 'Second'), ('Third', 'Third'), ('Fourth', 'Fourth')], default=' ', max_length=15),
        ),
        migrations.AlterField(
            model_name='semmaster',
            name='semid',
            field=models.CharField(max_length=6, validators=[django.core.validators.RegexValidator(message='Enter only integer.', regex='^[0-9]+$')]),
        ),
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
        migrations.AlterField(
            model_name='studentmaster',
            name='studentname',
            field=models.CharField(max_length=25, validators=[django.core.validators.RegexValidator(message='Only alphabetic characters are allowed.', regex='^[a-zA-Z]*$')]),
        ),
        migrations.AlterField(
            model_name='studentmaster',
            name='studentregno',
            field=models.CharField(max_length=6, validators=[django.core.validators.RegexValidator(message='Enter only integer.', regex='^[0-9]+$')]),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='batch_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.batchmaster'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.coursemaster'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='exam_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.exammaster'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='marks',
            field=models.CharField(max_length=3, validators=[django.core.validators.RegexValidator(message='Enter only integer.', regex='^[0-9]+$')]),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='paper_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.papermaster'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='semester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.semmaster'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='student_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.studentmaster'),
        ),
    ]
