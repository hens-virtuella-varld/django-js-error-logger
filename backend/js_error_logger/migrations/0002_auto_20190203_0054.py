# Generated by Django 2.1.5 on 2019-02-02 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('js_error_logger', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jserror',
            old_name='appId',
            new_name='app_id',
        ),
    ]
