# Generated by Django 3.2.9 on 2021-11-23 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_master_page_masterstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='master_page',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
