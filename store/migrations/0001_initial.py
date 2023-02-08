# Generated by Django 4.1.5 on 2023-02-03 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BuildingMaster',
            fields=[
                ('building_id', models.AutoField(primary_key=True, serialize=False)),
                ('building_name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeDesignationMaster',
            fields=[
                ('emp_des_id', models.AutoField(primary_key=True, serialize=False)),
                ('emp_des_name', models.CharField(max_length=250)),
                ('emp_des_type', models.CharField(choices=[('Judge', 'Judge'), ('Staff', 'Staff')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeDetails',
            fields=[
                ('emp_id', models.AutoField(primary_key=True, serialize=False)),
                ('emp_name', models.CharField(max_length=250)),
                ('emp_mobile', models.CharField(max_length=250)),
                ('entry_date', models.DateField(auto_now_add=True)),
                ('deleted', models.BooleanField(default=False)),
                ('emp_des_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.employeedesignationmaster')),
            ],
        ),
        migrations.CreateModel(
            name='HealthStatusDetails',
            fields=[
                ('health_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_id', models.IntegerField()),
                ('product_healthy', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10)),
                ('health_remarks', models.CharField(max_length=250)),
                ('product_status', models.CharField(choices=[('Working', 'Working'), ('Not Working', 'Not Working')], max_length=50)),
                ('status_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='LocationDetails',
            fields=[
                ('location_id', models.AutoField(primary_key=True, serialize=False)),
                ('floor', models.CharField(max_length=250)),
                ('roomno', models.CharField(max_length=250)),
                ('landmark', models.CharField(max_length=250)),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategoryMaster',
            fields=[
                ('product_cat_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_type', models.CharField(choices=[('Consumable', 'Consumable'), ('Non-Consumable', 'Non-Consumable')], max_length=20, verbose_name='Product Type')),
                ('product_cat_name', models.CharField(max_length=250, verbose_name='Product Category Name :')),
            ],
        ),
        migrations.CreateModel(
            name='ProductDetails',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=250)),
                ('product_model', models.CharField(max_length=250)),
                ('product_serialno', models.CharField(max_length=250)),
                ('entry_date', models.DateField(auto_now_add=True)),
                ('initial_quantity', models.IntegerField()),
                ('current_quantity', models.IntegerField()),
                ('remarks', models.CharField(max_length=300)),
                ('product_cat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.productcategorymaster')),
            ],
        ),
        migrations.CreateModel(
            name='TransactionDetails',
            fields=[
                ('trans_id', models.AutoField(primary_key=True, serialize=False)),
                ('trans_tpye', models.CharField(choices=[('Issued', 'Issued'), ('AtComputerSection', 'At Computer Section')], max_length=50)),
                ('trans_date', models.DateField()),
                ('remarks', models.CharField(max_length=250)),
                ('emp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.employeedetails')),
                ('location_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.locationdetails')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.productdetails')),
            ],
        ),
        migrations.CreateModel(
            name='SectionDetails',
            fields=[
                ('section_id', models.AutoField(primary_key=True, serialize=False)),
                ('section_type', models.CharField(choices=[('Court', 'Court'), ('Section', 'Section')], max_length=10)),
                ('section_name', models.CharField(max_length=250)),
                ('building_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.buildingmaster')),
            ],
        ),
        migrations.AddField(
            model_name='locationdetails',
            name='section_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.sectiondetails'),
        ),
    ]