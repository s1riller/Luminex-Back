# Generated by Django 4.2.6 on 2023-11-07 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_medicine_treats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='treats',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='api.answer'),
        ),
    ]
