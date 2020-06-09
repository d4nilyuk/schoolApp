# Generated by Django 3.0.6 on 2020-06-09 03:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolClass',
            fields=[
                ('schoolclass_name', models.CharField(max_length=30, verbose_name='Class name')),
                ('schoolclass_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Class',
                'verbose_name_plural': 'Classes',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('teacher_first_name', models.CharField(max_length=30, verbose_name='First Name')),
                ('teacher_last_name', models.CharField(max_length=30, verbose_name='Last Name')),
                ('teacher_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('hourlyRate', models.IntegerField()),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schoolapp.SchoolClass')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Teacher',
                'verbose_name_plural': 'Teachers',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_first_name', models.CharField(max_length=30, verbose_name='First Name')),
                ('student_last_name', models.CharField(max_length=30, verbose_name='Last Name')),
                ('student_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('attendence', models.BooleanField()),
                ('schoolClass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schoolapp.SchoolClass')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': 'Students',
            },
        ),
    ]
