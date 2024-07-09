# Generated by Django 5.0.6 on 2024-07-02 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_teacher_joined_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='To_msg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=400, null=True)),
                ('to_student', models.BinaryField()),
                ('to_teacher', models.BinaryField()),
            ],
        ),
    ]