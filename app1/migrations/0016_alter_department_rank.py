# Generated by Django 4.1.7 on 2023-03-25 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0015_alter_department_name_alter_department_rank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='rank',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
