# Generated by Django 4.1.5 on 2023-03-17 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_transactiondetails_location_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactiondetails',
            name='location_id',
        ),
        migrations.RemoveField(
            model_name='transactiondetails',
            name='no_of_item',
        ),
        migrations.RemoveField(
            model_name='transactiondetails',
            name='product_id',
        ),
        migrations.RemoveField(
            model_name='transactiondetails',
            name='remarks',
        ),
        migrations.RemoveField(
            model_name='transactiondetails',
            name='usr_id',
        ),
        migrations.CreateModel(
            name='ProductTransactionDetails',
            fields=[
                ('pro_trans_id', models.AutoField(primary_key=True, serialize=False)),
                ('no_of_item', models.IntegerField()),
                ('remarks', models.CharField(max_length=250)),
                ('location_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='store.locationdetails')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.productdetails')),
                ('trans_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.transactiondetails')),
                ('usr_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.userdetails')),
            ],
        ),
    ]
