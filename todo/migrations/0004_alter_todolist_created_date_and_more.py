# Generated by Django 4.2.2 on 2023-06-28 02:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0003_alter_todolist_created_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todolist",
            name="created_date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 6, 28, 2, 51, 46, 367656)
            ),
        ),
        migrations.AlterField(
            model_name="todolist",
            name="modified_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
