# Generated by Django 5.1 on 2024-08-15 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_remove_bookmodel_bookcontent_bookmodel_bookcontent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmodel',
            name='bookContent',
            field=models.FileField(upload_to='BookContent'),
        ),
    ]
