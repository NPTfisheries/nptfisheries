# Generated by Django 4.0.5 on 2022-10-24 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='points', to='locations.location'),
        ),
    ]
