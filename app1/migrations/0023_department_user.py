# Generated by Django 4.1.7 on 2023-03-27 13:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app1', '0022_alter_student_hsc_reg_alter_student_hsc_roll'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
