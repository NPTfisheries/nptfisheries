# Generated by Django 4.0.5 on 2022-10-20 19:26

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
        ('dfrm_admin', '0003_remove_facility_location_alter_department_facility_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subproject',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Subproject description'),
        ),
        migrations.AlterField(
            model_name='subproject',
            name='division',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_div', to='dfrm_admin.division', verbose_name='Subproject division'),
        ),
        migrations.AlterField(
            model_name='subproject',
            name='supervisor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_sup', to='dfrm_admin.employee', verbose_name='Subproject supervisor'),
        ),
        migrations.AlterField(
            model_name='task',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.location', verbose_name='Task location'),
        ),
        migrations.AlterField(
            model_name='task',
            name='staff',
            field=models.ManyToManyField(blank=True, related_name='staff', to='dfrm_admin.employee', verbose_name='Task staff'),
        ),
        migrations.AlterField(
            model_name='task',
            name='supervisor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_sup', to='dfrm_admin.employee', verbose_name='Task supervisor'),
        ),
    ]