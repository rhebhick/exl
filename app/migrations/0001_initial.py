# Generated by Django 5.0.6 on 2024-06-27 07:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Classhave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classes', models.CharField(max_length=180)),
                ('desc', models.CharField(max_length=360, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=180)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=180)),
                ('last_name', models.CharField(max_length=180)),
                ('email', models.CharField(max_length=180)),
                ('dob', models.DateField()),
                ('father', models.CharField(max_length=180)),
                ('mother', models.CharField(max_length=180)),
                ('father_occupation', models.CharField(max_length=180)),
                ('mother_occupation', models.CharField(max_length=180)),
                ('password', models.CharField(max_length=180)),
                ('joined_date', models.DateField(auto_now_add=True, null=True)),
                ('to_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=180, null=True)),
                ('last_name', models.CharField(max_length=180, null=True)),
                ('dob', models.DateField(null=True)),
                ('email', models.CharField(max_length=180, null=True)),
                ('hse_board', models.CharField(max_length=180, null=True)),
                ('hse_percent', models.IntegerField(null=True)),
                ('degree', models.CharField(max_length=180, null=True)),
                ('score', models.IntegerField(null=True)),
                ('password', models.CharField(max_length=180, null=True)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.department')),
                ('to_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]