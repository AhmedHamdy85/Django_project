# Generated by Django 5.1.6 on 2025-03-05 06:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0007_remove_project_is_selected_selectedproject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selectedproject',
            name='project',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='homepage.project'),
        ),
    ]
