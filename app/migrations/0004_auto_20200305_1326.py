# Generated by Django 3.0.3 on 2020-03-05 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_like_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='content',
            new_name='comment',
        ),
    ]
