# Generated by Django 4.1.7 on 2023-03-25 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0016_alter_department_rank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='roll',
            field=models.CharField(max_length=10, null=True, unique=True),
        ),
    ]