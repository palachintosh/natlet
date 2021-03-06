# Generated by Django 2.2.10 on 2020-03-02 21:45

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novatlet', '0022_auto_20200302_0816'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='boolean',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='photos',
            name='img_object',
            field=models.ImageField(db_index=True, storage=django.core.files.storage.FileSystemStorage(location='my_dir/photos/\n'), upload_to='', verbose_name='Images'),
        ),
    ]
