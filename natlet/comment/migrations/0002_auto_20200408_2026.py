# Generated by Django 2.2.10 on 2020-04-08 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='moderate',
            field=models.BooleanField(default=False, verbose_name='Опубликовать!'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.CharField(db_index=True, max_length=700, verbose_name='Коментар: '),
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=180, verbose_name="Ваше iм'я: "),
        ),
    ]
