# Generated by Django 4.1.13 on 2024-07-26 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multihospital_app', '0002_hospitalavail_availabilitylist_hospitalavail_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospitalavail',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='hospital_images/'),
        ),
    ]