# Generated by Django 4.2.6 on 2023-10-24 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_user_date_of_birth_user_birth_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imperfection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
    ]