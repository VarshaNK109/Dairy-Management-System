# Generated by Django 2.1.7 on 2019-03-03 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dairyapp', '0003_remove_vendorledger_milktype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addvendor',
            name='vendorname',
            field=models.CharField(db_index=True, max_length=200, unique=True),
        ),
    ]
