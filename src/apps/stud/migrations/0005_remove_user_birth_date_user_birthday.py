# Generated by Django 4.1.4 on 2023-01-14 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stud', '0004_user_birth_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='birth_date',
        ),
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateField(null=True, verbose_name='Birthday'),
        ),
    ]