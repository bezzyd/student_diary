# Generated by Django 4.1.5 on 2023-01-22 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stud", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="birth_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]
