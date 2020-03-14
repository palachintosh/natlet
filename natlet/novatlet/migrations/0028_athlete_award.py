# Generated by Django 2.2.10 on 2020-03-10 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novatlet', '0027_auto_20200305_2005'),
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=300)),
                ('city', models.CharField(max_length=100)),
                ('score_year', models.DateField()),
                ('count', models.PositiveIntegerField()),
                ('award_icon', models.ImageField(db_index=True, upload_to='images/award_icon/', verbose_name='aw_icons')),
            ],
        ),
        migrations.CreateModel(
            name='Athlete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150)),
                ('second_name', models.CharField(db_index=True, max_length=150)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('birth_year', models.DateField()),
                ('description', models.TextField(blank=True)),
                ('picture', models.ImageField(db_index=True, default='images/image.jpg', upload_to='images/athletes/')),
                ('athletes_awards', models.ManyToManyField(blank=True, related_name='athletes_aw', to='novatlet.Award')),
            ],
        ),
    ]
