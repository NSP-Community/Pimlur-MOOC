# Generated by Django 2.2.3 on 2023-07-16 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PimlurMOOC', '0005_auto_20230716_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='pimluritem',
            name='name',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='pimlur',
            name='name',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='pimlurcategory',
            name='name',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='pimlursubcategory',
            name='name',
            field=models.CharField(default='', max_length=300),
        ),
    ]
