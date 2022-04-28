# Generated by Django 4.0.2 on 2022-04-15 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
                ('phone', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('mobile', models.CharField(max_length=100, null=True)),
                ('password', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('owner', models.CharField(blank=True, max_length=1000, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('addres', models.CharField(blank=True, max_length=10000, null=True)),
                ('area', models.CharField(blank=True, max_length=1000, null=True)),
                ('opentime', models.TimeField(blank=True, null=True)),
                ('closestime', models.TimeField(blank=True, null=True)),
                ('restImage', models.ImageField(upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Menu', models.CharField(max_length=3000)),
                ('spacial', models.CharField(blank=True, max_length=3000, null=True)),
                ('offer', models.CharField(blank=True, max_length=3000, null=True)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Mainapp.restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=3000)),
                ('food_prize', models.PositiveIntegerField()),
                ('veg', models.BooleanField(blank=True, null=True)),
                ('nonveg', models.BooleanField(blank=True, null=True)),
                ('egg', models.BooleanField(blank=True, null=True)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Mainapp.menu')),
            ],
        ),
    ]
