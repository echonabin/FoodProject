# Generated by Django 4.0.3 on 2022-04-24 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mainapp', '0005_remove_restaurant_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='des',
            field=models.TextField(blank=True, max_length=10000, null=True),
        ),
    ]