# Generated by Django 5.1.6 on 2025-03-03 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_alter_user_image_alter_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='static/images/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.FileField(default='', upload_to='static/images/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
