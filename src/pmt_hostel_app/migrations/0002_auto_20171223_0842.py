# Generated by Django 2.0 on 2017-12-23 03:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pmt_hostel_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(help_text='Enter your full name', max_length=100)),
                ('email', models.EmailField(help_text='Enter your email, eg. rishikesh0014051992@gmail.com', max_length=100, unique=True)),
                ('contact', models.CharField(help_text='Enter your 10 digit mobile number', max_length=10)),
                ('dob', models.DateField(help_text='Enter your date of birth')),
                ('password', models.CharField(help_text='Enter your password', max_length=20)),
                ('quote', models.TextField(blank=True, help_text='Enter your popular quote, eg. Never give up and try to achieve your goal with passion', null=True)),
                ('batch', models.IntegerField(default=2017, help_text='From which batch you are, eg. 2017, 2015, 2011 etc.', validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2017)])),
                ('is_admin', models.BooleanField(default=False, help_text='Hi Admin, you want make this person as admin?')),
                ('account_confirmed', models.BooleanField(default=False, help_text='User has confirmed his account or not')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='The time when user registered')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Last time when he updated the details')),
            ],
        ),
        migrations.DeleteModel(
            name='PmtStudent',
        ),
    ]
