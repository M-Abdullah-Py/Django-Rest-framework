# Generated by Django 5.1.2 on 2024-10-18 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.IntegerField()),
                ('name', models.CharField(max_length=20)),
                ('branch', models.CharField(max_length=50)),
            ],
        ),
    ]
