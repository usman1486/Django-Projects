# Generated by Django 4.1.2 on 2022-11-27 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0002_alter_information_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='information',
            name='gender',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='information',
            name='img',
            field=models.ImageField(default=None, upload_to=''),
        ),
    ]
