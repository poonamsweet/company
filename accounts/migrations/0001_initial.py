# Generated by Django 3.0.7 on 2020-10-10 10:22

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_se', models.BooleanField(default=False)),
                ('is_abm', models.BooleanField(default=False)),
                ('is_rbm', models.BooleanField(default=False)),
                ('is_zbm', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('username', models.CharField(max_length=15, unique=True)),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('mobile_number', models.CharField(blank=True, max_length=15, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Abm',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accounts.User')),
                ('area', models.CharField(max_length=15)),
                ('birthdate', models.DateField(auto_now_add=True)),
                ('gender', models.CharField(choices=[('Select', 'Select'), ('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('height', models.CharField(blank=True, max_length=8, null=True)),
                ('weight', models.CharField(blank=True, max_length=7, null=True)),
                ('identification_mark', models.CharField(blank=True, max_length=50, null=True)),
                ('blood_group', models.CharField(blank=True, max_length=3, null=True)),
                ('maritual_status', models.CharField(choices=[('select', 'Select'), ('Married', 'Married'), ('Single', 'Single')], max_length=20)),
                ('marriage_date', models.DateField(auto_now_add=True)),
                ('Nationality', models.CharField(max_length=6)),
                ('address_line_1', models.CharField(max_length=30)),
                ('address_line_2', models.CharField(max_length=30)),
                ('pin', models.CharField(max_length=6)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=30)),
                ('mailing_address', models.CharField(choices=[('select', 'Select'), ('Same', 'Same'), ('Different', 'Different')], max_length=20)),
                ('mail_address_line_1', models.CharField(max_length=30)),
                ('mail_address_line_2', models.CharField(max_length=30)),
                ('mail_pin', models.CharField(max_length=6)),
                ('mail_city', models.CharField(max_length=15)),
                ('mail_state', models.CharField(max_length=30)),
                ('bank_name', models.CharField(max_length=20)),
                ('account_no', models.CharField(max_length=20)),
                ('pan_no', models.CharField(max_length=20)),
                ('pan_pic', models.ImageField(upload_to='')),
                ('passport_no', models.CharField(max_length=20)),
                ('passport_pic', models.FileField(upload_to='')),
                ('driving_license', models.CharField(max_length=20)),
                ('driving_license_pic', models.FileField(upload_to='')),
                ('high_school', models.CharField(max_length=30)),
                ('high_school_passing_year', models.CharField(max_length=4)),
                ('high_school_marks_obtained', models.CharField(max_length=5)),
                ('high_school_cert', models.FileField(upload_to='')),
                ('intermediate_school', models.CharField(max_length=30)),
                ('intermediate_passing_year', models.CharField(max_length=4)),
                ('intermediate_marks_obtained', models.CharField(max_length=5)),
                ('intermediate_cert', models.FileField(upload_to='')),
                ('Degree_obtained', models.CharField(max_length=30)),
                ('college_institute', models.CharField(max_length=50)),
                ('Year_of_passing', models.CharField(max_length=4)),
                ('marks_obtained', models.CharField(max_length=5)),
                ('degree_cert', models.FileField(upload_to='')),
                ('experience', models.CharField(choices=[('select', 'Select'), ('Yes', 'Yes'), ('No', 'No')], max_length=20)),
                ('organisation_name', models.CharField(max_length=50)),
                ('position_held', models.CharField(max_length=20)),
                ('head_quater', models.CharField(max_length=50)),
                ('date_of_joining', models.DateField(blank=True, null=True)),
                ('date_of_leaving', models.DateField(blank=True, null=True)),
                ('father_name', models.CharField(max_length=20)),
                ('mother_name', models.CharField(max_length=20)),
                ('brother', models.CharField(max_length=1)),
                ('sister', models.CharField(max_length=1)),
                ('spouse_name', models.CharField(max_length=20)),
                ('children_count', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accounts.User')),
                ('company', models.CharField(blank=True, max_length=15, null=True)),
                ('birthdate', models.DateField(auto_now_add=True)),
                ('gender', models.CharField(choices=[('Select', 'Select'), ('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('height', models.CharField(blank=True, max_length=8, null=True)),
                ('weight', models.CharField(blank=True, max_length=7, null=True)),
                ('identification_mark', models.CharField(blank=True, max_length=50, null=True)),
                ('blood_group', models.CharField(blank=True, max_length=3, null=True)),
                ('maritual_status', models.CharField(choices=[('select', 'Select'), ('Married', 'Married'), ('Single', 'Single')], max_length=20)),
                ('marriage_date', models.DateField(auto_now_add=True)),
                ('Nationality', models.CharField(max_length=6)),
                ('address_line_1', models.CharField(max_length=30)),
                ('address_line_2', models.CharField(max_length=30)),
                ('pin', models.CharField(max_length=6)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=30)),
                ('mailing_address', models.CharField(choices=[('select', 'Select'), ('Same', 'Same'), ('Different', 'Different')], max_length=20)),
                ('mail_address_line_1', models.CharField(max_length=30)),
                ('mail_address_line_2', models.CharField(max_length=30)),
                ('mail_pin', models.CharField(max_length=6)),
                ('mail_city', models.CharField(max_length=15)),
                ('mail_state', models.CharField(max_length=30)),
                ('bank_name', models.CharField(max_length=20)),
                ('account_no', models.CharField(max_length=20)),
                ('pan_no', models.CharField(max_length=20)),
                ('pan_pic', models.ImageField(upload_to='')),
                ('passport_no', models.CharField(max_length=20)),
                ('passport_pic', models.FileField(upload_to='')),
                ('driving_license', models.CharField(max_length=20)),
                ('driving_license_pic', models.FileField(upload_to='')),
                ('high_school', models.CharField(max_length=30)),
                ('high_school_passing_year', models.CharField(max_length=4)),
                ('high_school_marks_obtained', models.CharField(max_length=5)),
                ('high_school_cert', models.FileField(upload_to='')),
                ('intermediate_school', models.CharField(max_length=30)),
                ('intermediate_passing_year', models.CharField(max_length=4)),
                ('intermediate_marks_obtained', models.CharField(max_length=5)),
                ('intermediate_cert', models.FileField(upload_to='')),
                ('Degree_obtained', models.CharField(max_length=30)),
                ('college_institute', models.CharField(max_length=50)),
                ('Year_of_passing', models.CharField(max_length=4)),
                ('marks_obtained', models.CharField(max_length=5)),
                ('degree_cert', models.FileField(upload_to='')),
                ('experience', models.CharField(choices=[('select', 'Select'), ('Yes', 'Yes'), ('No', 'No')], max_length=20)),
                ('organisation_name', models.CharField(max_length=50)),
                ('position_held', models.CharField(max_length=20)),
                ('head_quater', models.CharField(max_length=50)),
                ('date_of_joining', models.DateField(blank=True, null=True)),
                ('date_of_leaving', models.DateField(blank=True, null=True)),
                ('father_name', models.CharField(max_length=20)),
                ('mother_name', models.CharField(max_length=20)),
                ('brother', models.CharField(max_length=1)),
                ('sister', models.CharField(max_length=1)),
                ('spouse_name', models.CharField(max_length=20)),
                ('children_count', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Rbm',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accounts.User')),
                ('region', models.CharField(blank=True, max_length=15, null=True)),
                ('birthdate', models.DateField(auto_now_add=True)),
                ('gender', models.CharField(choices=[('Select', 'Select'), ('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('height', models.CharField(blank=True, max_length=8, null=True)),
                ('weight', models.CharField(blank=True, max_length=7, null=True)),
                ('identification_mark', models.CharField(blank=True, max_length=50, null=True)),
                ('blood_group', models.CharField(blank=True, max_length=3, null=True)),
                ('maritual_status', models.CharField(choices=[('select', 'Select'), ('Married', 'Married'), ('Single', 'Single')], max_length=20)),
                ('marriage_date', models.DateField(auto_now_add=True)),
                ('Nationality', models.CharField(max_length=6)),
                ('address_line_1', models.CharField(max_length=30)),
                ('address_line_2', models.CharField(max_length=30)),
                ('pin', models.CharField(max_length=6)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=30)),
                ('mailing_address', models.CharField(choices=[('select', 'Select'), ('Same', 'Same'), ('Different', 'Different')], max_length=20)),
                ('mail_address_line_1', models.CharField(max_length=30)),
                ('mail_address_line_2', models.CharField(max_length=30)),
                ('mail_pin', models.CharField(max_length=6)),
                ('mail_city', models.CharField(max_length=15)),
                ('mail_state', models.CharField(max_length=30)),
                ('bank_name', models.CharField(max_length=20)),
                ('account_no', models.CharField(max_length=20)),
                ('pan_no', models.CharField(max_length=20)),
                ('pan_pic', models.ImageField(upload_to='')),
                ('passport_no', models.CharField(max_length=20)),
                ('passport_pic', models.FileField(upload_to='')),
                ('driving_license', models.CharField(max_length=20)),
                ('driving_license_pic', models.FileField(upload_to='')),
                ('high_school', models.CharField(max_length=30)),
                ('high_school_passing_year', models.CharField(max_length=4)),
                ('high_school_marks_obtained', models.CharField(max_length=5)),
                ('high_school_cert', models.FileField(upload_to='')),
                ('intermediate_school', models.CharField(max_length=30)),
                ('intermediate_passing_year', models.CharField(max_length=4)),
                ('intermediate_marks_obtained', models.CharField(max_length=5)),
                ('intermediate_cert', models.FileField(upload_to='')),
                ('Degree_obtained', models.CharField(max_length=30)),
                ('college_institute', models.CharField(max_length=50)),
                ('Year_of_passing', models.CharField(max_length=4)),
                ('marks_obtained', models.CharField(max_length=5)),
                ('degree_cert', models.FileField(upload_to='')),
                ('experience', models.CharField(choices=[('select', 'Select'), ('Yes', 'Yes'), ('No', 'No')], max_length=20)),
                ('organisation_name', models.CharField(max_length=50)),
                ('position_held', models.CharField(max_length=20)),
                ('head_quater', models.CharField(max_length=50)),
                ('date_of_joining', models.DateField(blank=True, null=True)),
                ('date_of_leaving', models.DateField(blank=True, null=True)),
                ('father_name', models.CharField(max_length=20)),
                ('mother_name', models.CharField(max_length=20)),
                ('brother', models.CharField(max_length=1)),
                ('sister', models.CharField(max_length=1)),
                ('spouse_name', models.CharField(max_length=20)),
                ('children_count', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Zbm',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accounts.User')),
                ('zone', models.CharField(blank=True, max_length=15, null=True)),
                ('birthdate', models.DateField(auto_now_add=True)),
                ('gender', models.CharField(choices=[('Select', 'Select'), ('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('height', models.CharField(blank=True, max_length=8, null=True)),
                ('weight', models.CharField(blank=True, max_length=7, null=True)),
                ('identification_mark', models.CharField(blank=True, max_length=50, null=True)),
                ('blood_group', models.CharField(blank=True, max_length=3, null=True)),
                ('maritual_status', models.CharField(choices=[('select', 'Select'), ('Married', 'Married'), ('Single', 'Single')], max_length=20)),
                ('marriage_date', models.DateField(auto_now_add=True)),
                ('Nationality', models.CharField(max_length=6)),
                ('address_line_1', models.CharField(max_length=30)),
                ('address_line_2', models.CharField(max_length=30)),
                ('pin', models.CharField(max_length=6)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=30)),
                ('mailing_address', models.CharField(choices=[('select', 'Select'), ('Same', 'Same'), ('Different', 'Different')], max_length=20)),
                ('mail_address_line_1', models.CharField(max_length=30)),
                ('mail_address_line_2', models.CharField(max_length=30)),
                ('mail_pin', models.CharField(max_length=6)),
                ('mail_city', models.CharField(max_length=15)),
                ('mail_state', models.CharField(max_length=30)),
                ('bank_name', models.CharField(max_length=20)),
                ('account_no', models.CharField(max_length=20)),
                ('pan_no', models.CharField(max_length=20)),
                ('pan_pic', models.ImageField(upload_to='')),
                ('passport_no', models.CharField(max_length=20)),
                ('passport_pic', models.FileField(upload_to='')),
                ('driving_license', models.CharField(max_length=20)),
                ('driving_license_pic', models.FileField(upload_to='')),
                ('high_school', models.CharField(max_length=30)),
                ('high_school_passing_year', models.CharField(max_length=4)),
                ('high_school_marks_obtained', models.CharField(max_length=5)),
                ('high_school_cert', models.FileField(upload_to='')),
                ('intermediate_school', models.CharField(max_length=30)),
                ('intermediate_passing_year', models.CharField(max_length=4)),
                ('intermediate_marks_obtained', models.CharField(max_length=5)),
                ('intermediate_cert', models.FileField(upload_to='')),
                ('Degree_obtained', models.CharField(max_length=30)),
                ('college_institute', models.CharField(max_length=50)),
                ('Year_of_passing', models.CharField(max_length=4)),
                ('marks_obtained', models.CharField(max_length=5)),
                ('degree_cert', models.FileField(upload_to='')),
                ('experience', models.CharField(choices=[('select', 'Select'), ('Yes', 'Yes'), ('No', 'No')], max_length=20)),
                ('organisation_name', models.CharField(max_length=50)),
                ('position_held', models.CharField(max_length=20)),
                ('head_quater', models.CharField(max_length=50)),
                ('date_of_joining', models.DateField(blank=True, null=True)),
                ('date_of_leaving', models.DateField(blank=True, null=True)),
                ('father_name', models.CharField(max_length=20)),
                ('mother_name', models.CharField(max_length=20)),
                ('brother', models.CharField(max_length=1)),
                ('sister', models.CharField(max_length=1)),
                ('spouse_name', models.CharField(max_length=20)),
                ('children_count', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Salesexecutive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, max_length=50, null=True)),
                ('birthdate', models.DateField(auto_now_add=True)),
                ('gender', models.CharField(choices=[('Select', 'Select'), ('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('height', models.CharField(blank=True, max_length=8, null=True)),
                ('weight', models.CharField(blank=True, max_length=7, null=True)),
                ('identification_mark', models.CharField(blank=True, max_length=50, null=True)),
                ('blood_group', models.CharField(blank=True, max_length=3, null=True)),
                ('maritual_status', models.CharField(choices=[('select', 'Select'), ('Married', 'Married'), ('Single', 'Single')], max_length=20)),
                ('marriage_date', models.DateField(auto_now_add=True)),
                ('Nationality', models.CharField(max_length=6)),
                ('address_line_1', models.CharField(max_length=30)),
                ('address_line_2', models.CharField(max_length=30)),
                ('pin', models.CharField(max_length=6)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=30)),
                ('mailing_address', models.CharField(choices=[('select', 'Select'), ('Same', 'Same'), ('Different', 'Different')], max_length=20)),
                ('mail_address_line_1', models.CharField(max_length=30)),
                ('mail_address_line_2', models.CharField(max_length=30)),
                ('mail_pin', models.CharField(max_length=6)),
                ('mail_city', models.CharField(max_length=15)),
                ('mail_state', models.CharField(max_length=30)),
                ('bank_name', models.CharField(max_length=20)),
                ('account_no', models.CharField(max_length=20)),
                ('pan_no', models.CharField(max_length=20)),
                ('pan_pic', models.ImageField(upload_to='')),
                ('passport_no', models.CharField(max_length=20)),
                ('passport_pic', models.FileField(upload_to='')),
                ('driving_license', models.CharField(max_length=20)),
                ('driving_license_pic', models.FileField(upload_to='')),
                ('high_school', models.CharField(max_length=30)),
                ('high_school_passing_year', models.CharField(max_length=4)),
                ('high_school_marks_obtained', models.CharField(max_length=5)),
                ('high_school_cert', models.FileField(upload_to='')),
                ('intermediate_school', models.CharField(max_length=30)),
                ('intermediate_passing_year', models.CharField(max_length=5)),
                ('intermediate_marks_obtained', models.CharField(max_length=4)),
                ('intermediate_cert', models.FileField(upload_to='')),
                ('Degree_obtained', models.CharField(max_length=30)),
                ('college_institute', models.CharField(max_length=50)),
                ('Year_of_passing', models.CharField(max_length=4)),
                ('marks_obtained', models.CharField(max_length=5)),
                ('degree_cert', models.FileField(upload_to='')),
                ('experience', models.CharField(choices=[('select', 'Select'), ('Yes', 'Yes'), ('No', 'No')], max_length=20)),
                ('organisation_name', models.CharField(max_length=50)),
                ('position_held', models.CharField(max_length=20)),
                ('head_quater', models.CharField(max_length=50)),
                ('date_of_joining', models.DateField(blank=True, null=True)),
                ('date_of_leaving', models.DateField(blank=True, null=True)),
                ('father_name', models.CharField(max_length=20)),
                ('mother_name', models.CharField(max_length=20)),
                ('brother', models.CharField(max_length=1)),
                ('sister', models.CharField(max_length=1)),
                ('spouse_name', models.CharField(max_length=20)),
                ('children_count', models.CharField(max_length=1)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.User')),
            ],
        ),
    ]