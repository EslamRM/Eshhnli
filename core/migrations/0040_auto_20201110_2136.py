# Generated by Django 2.2.12 on 2020-11-10 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0039_auto_20201110_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address_1',
            field=models.CharField(default='', help_text='Address 1', max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='address_2',
            field=models.CharField(default='es', help_text='Address 2', max_length=500),
            preserve_default=False,
        ),
    ]
