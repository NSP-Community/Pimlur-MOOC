# Generated by Django 2.2.3 on 2023-07-16 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PimlurMOOC', '0003_auto_20230715_2316'),
    ]

    operations = [
        migrations.AddField(
            model_name='pimluruser',
            name='PimlurCategory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='PimlurMOOC.PimlurCategory'),
            preserve_default=False,
        ),
    ]
