# Generated by Django 5.0.6 on 2024-05-23 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('money_calc', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='agent_name',
            new_name='agent',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='worker_name',
            new_name='worker',
        ),
    ]
