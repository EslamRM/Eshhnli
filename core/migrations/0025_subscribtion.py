# Generated by Django 2.2.12 on 2020-11-09 13:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0024_auto_20201107_1032'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribtion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscribe', models.CharField(help_text='Subscribe', max_length=300)),
                ('user', models.ForeignKey(help_text='User', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
