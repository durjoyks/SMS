# Generated by Django 4.1.7 on 2023-03-26 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0020_student_hsc_reg_student_hsc_roll_alter_student_dept'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='hsc_roll',
            field=models.CharField(max_length=16, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='reg_no',
            field=models.CharField(blank=True, max_length=16, null=True, unique=True),
        ),
    ]
