# Generated by Django 3.0.7 on 2020-10-18 04:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('report', '0004_auto_20201018_0339'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonthlyplanList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('dr_speciality', models.CharField(choices=[('NEUROLOGIST', 'NEUROLOGIST'), ('NEUROSURGEON', 'NEUROSURGEON'), ('PSYCHIATRIST', 'PSYCHIATRIST'), ('PHYSICIAN', 'PHYSICIAN'), ('GENRAL PHYSICIAN', 'GENRAL PHYSICIAN'), ('GYNAECOLOGIST', 'GYNAECOLOGIST'), ('SURGEON', 'SURGEON'), ('ORTHOLOGIST', 'ORTHOLOGIST')], max_length=100)),
                ('dr_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='report.DrMasterList')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.User')),
            ],
        ),
        migrations.AlterField(
            model_name='dailydrcallreport',
            name='dr_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='report.MonthlyplanList'),
        ),
    ]
