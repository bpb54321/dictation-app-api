# Generated by Django 2.1.1 on 2018-09-15 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0005_auto_20180915_2058'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mediaitem',
            options={'ordering': ('title',)},
        ),
    ]