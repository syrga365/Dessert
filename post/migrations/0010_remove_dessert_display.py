# Generated by Django 4.2.9 on 2024-02-05 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_dessert_display'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dessert',
            name='display',
        ),
    ]
