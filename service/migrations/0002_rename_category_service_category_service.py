# Generated by Django 4.2.3 on 2023-07-10 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='category',
            new_name='category_service',
        ),
    ]
