# Generated by Django 4.1.5 on 2023-03-26 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_birth_date_alter_user_profile_photo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_type',
            field=models.IntegerField(blank=True, choices=[(1, 'Student'), (2, 'Teacher')], null=True),
        ),
    ]