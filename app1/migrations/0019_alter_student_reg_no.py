# Generated by Django 4.1.7 on 2023-03-25 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0018_alter_student_reg_no_alter_student_roll'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='reg_no',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True),
        ),
    ]