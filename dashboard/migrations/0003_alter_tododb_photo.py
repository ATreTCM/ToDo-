# Generated by Django 4.0.4 on 2022-05-03 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_alter_tododb_date_add_alter_tododb_date_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tododb',
            name='photo',
            field=models.ImageField(upload_to='uploads/%Y/%m/%d/'),
        ),
    ]
