# Generated by Django 4.1.1 on 2022-11-30 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('credentials', '0002_mymodel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Country',
            new_name='District',
        ),
        migrations.DeleteModel(
            name='MyModel',
        ),
    ]
