# Generated by Django 2.2.12 on 2020-11-09 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_auto_20201109_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribtion',
            name='subscribe',
            field=models.CharField(choices=[('No_Limits', 'No Limits'), ('More_Discount', 'More Discount'), ('Platinum', 'Platinum')], help_text='Subscribe', max_length=1),
        ),
    ]