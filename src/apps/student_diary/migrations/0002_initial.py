# Generated by Django 4.1.5 on 2023-03-22 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('student_diary', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentdiary',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_diary', to='users.studentprofile'),
        ),
    ]
