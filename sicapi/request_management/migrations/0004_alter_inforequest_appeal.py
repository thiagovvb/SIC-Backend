# Generated by Django 4.0.3 on 2022-04-16 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('request_management', '0003_remove_infoappeal_original_request_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inforequest',
            name='appeal',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='request_management.infoappeal'),
        ),
    ]
