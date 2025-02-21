# Generated by Django 5.1.6 on 2025-02-21 12:16

import core.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('firstName', models.CharField(max_length=25)),
                ('lastName', models.CharField(max_length=35)),
                ('phoneNumber', models.PositiveIntegerField(validators=[core.validators.validate_length])),
                ('password', models.CharField(max_length=16, validators=[django.core.validators.MinLengthValidator(8, 'password must be between 8 to 16 character')])),
                ('address', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
