# Generated by Django 4.0.4 on 2022-06-02 04:13

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0005_personalinfo_remove_userprofile_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinfo',
            name='city_name',
            field=models.CharField(max_length=225),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='mobile',
            field=phone_field.models.PhoneField(blank=True, max_length=31),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='notes_for_address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='street_address',
            field=models.CharField(max_length=225),
        ),
    ]
