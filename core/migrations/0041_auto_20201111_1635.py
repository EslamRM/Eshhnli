# Generated by Django 2.2.12 on 2020-11-11 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0040_auto_20201110_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address_2',
            field=models.CharField(blank=True, help_text='Address 2', max_length=500, null=True),
        ),
    ]