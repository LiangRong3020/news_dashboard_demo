# Generated by Django 2.1.3 on 2018-11-21 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('text', '0007_auto_20181119_1358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='negative',
        ),
        migrations.RemoveField(
            model_name='content',
            name='positive',
        ),
        migrations.RemoveField(
            model_name='content',
            name='pushauthor',
        ),
        migrations.RemoveField(
            model_name='content',
            name='pushcontent',
        ),
        migrations.RemoveField(
            model_name='content',
            name='pushdate',
        ),
    ]
