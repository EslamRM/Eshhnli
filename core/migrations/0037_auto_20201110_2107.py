# Generated by Django 2.2.12 on 2020-11-10 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0036_auto_20201110_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribtion',
            name='subscribe',
            field=models.CharField(choices=[('More_Discount', 'More Discount'), ('Platinum', 'Platinum'), ('No_Limits', 'No Limits')], help_text='Subscribe', max_length=50),
        ),
    ]
