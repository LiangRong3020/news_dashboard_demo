# Generated by Django 2.1.3 on 2018-11-19 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('text', '0004_auto_20181119_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='pushdate',
            field=models.DateTimeField(null=True),
        ),
    ]
