# Generated by Django 2.2.10 on 2020-03-02 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novatlet', '0020_auto_20200301_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='dir_object',
            field=models.CharField(blank=True, db_index=True, default='', max_length=100, unique=True),
        ),
    ]
