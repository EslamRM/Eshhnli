# Generated by Django 2.2.12 on 2020-11-09 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_auto_20201109_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribtion',
            name='subscribe',
            field=models.CharField(choices=[('No_Limits', 'No Limits'), ('Platinum', 'Platinum'), ('More_Discount', 'More Discount')], help_text='Subscribe', max_length=50),
        ),
    ]