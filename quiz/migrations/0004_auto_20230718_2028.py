# Generated by Django 2.2.3 on 2023-07-18 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_auto_20230718_2027'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='name',
            new_name='value',
        ),
    ]
