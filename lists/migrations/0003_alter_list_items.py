# Generated by Django 3.2.7 on 2021-09-10 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_alter_list_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='items',
            field=models.JSONField(default=[]),
        ),
    ]
