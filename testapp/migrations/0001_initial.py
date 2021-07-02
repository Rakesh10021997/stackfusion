# Generated by Django 3.1.1 on 2021-06-30 09:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default=' ', max_length=20, null=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only characters are allowed.')])),
                ('dob', models.DateField()),
                ('email', models.EmailField(default=' ', max_length=100, null=True)),
                ('mobilenumber', models.CharField(max_length=10, null=True, validators=[django.core.validators.RegexValidator('^[0-9]{10}$', 'Only digits are allowed.')])),
            ],
        ),
    ]
