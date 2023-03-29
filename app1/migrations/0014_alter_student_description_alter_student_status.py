# Generated by Django 4.1.7 on 2023-03-23 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_student_status_alter_student_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='description',
            field=models.CharField(blank=True, max_length=3000, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Accecpted', 'Accecpted')], default='Pending', max_length=40, null=True),
        ),
    ]
