# Generated by Django 2.2.10 on 2020-02-25 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('novatlet', '0003_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dir_object', models.CharField(default='', max_length=100, verbose_name='Location')),
            ],
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_object', models.ImageField(upload_to='photos/')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='novatlet.Location')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='related_gallery',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='novatlet.Location'),
        ),
    ]
