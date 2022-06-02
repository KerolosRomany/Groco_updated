# Generated by Django 4.0.4 on 2022-06-02 00:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0005_personalinfo_remove_userprofile_address_and_more'),
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='shipping',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='userprofile.personalinfo'),
        ),
    ]
