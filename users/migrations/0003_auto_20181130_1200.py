# Generated by Django 2.1.3 on 2018-11-30 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20181130_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='profile_pics/default.jpeg', upload_to='profile_pics'),
        ),
    ]
