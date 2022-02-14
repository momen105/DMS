# Generated by Django 4.0.1 on 2022-02-13 12:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SellerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_pics')),
                ('description', models.TextField(blank=True)),
                ('full_name', models.CharField(blank=True, max_length=264)),
                ('dob', models.DateField(blank=True, null=True)),
                ('website', models.URLField(blank=True)),
                ('facebook', models.URLField(blank=True)),
                ('nid_number', models.CharField(blank=True, max_length=40)),
                ('address_1', models.TextField(blank=True, max_length=300)),
                ('city', models.CharField(blank=True, max_length=40)),
                ('zipcode', models.CharField(blank=True, max_length=10)),
                ('country', models.CharField(blank=True, max_length=50)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='seller_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_pics')),
                ('description', models.TextField(blank=True)),
                ('full_name', models.CharField(blank=True, max_length=264)),
                ('dob', models.DateField(blank=True, null=True)),
                ('website', models.URLField(blank=True)),
                ('facebook', models.URLField(blank=True)),
                ('nid_number', models.CharField(blank=True, max_length=40)),
                ('address_1', models.TextField(blank=True, max_length=300)),
                ('city', models.CharField(blank=True, max_length=40)),
                ('zipcode', models.CharField(blank=True, max_length=10)),
                ('country', models.CharField(blank=True, max_length=50)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='employee_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AdminProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_pics')),
                ('description', models.TextField(blank=True)),
                ('full_name', models.CharField(blank=True, max_length=264)),
                ('dob', models.DateField(blank=True, null=True)),
                ('website', models.URLField(blank=True)),
                ('facebook', models.URLField(blank=True)),
                ('nid_number', models.CharField(blank=True, max_length=40)),
                ('address_1', models.TextField(blank=True, max_length=300)),
                ('city', models.CharField(blank=True, max_length=40)),
                ('zipcode', models.CharField(blank=True, max_length=10)),
                ('country', models.CharField(blank=True, max_length=50)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='admin_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
