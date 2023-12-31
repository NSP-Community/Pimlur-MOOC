# Generated by Django 2.2.3 on 2023-07-18 18:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_auto_20230718_2028'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('PimlurMOOC', '0007_pimlursubcategory_pimlur'),
    ]

    operations = [
        migrations.AddField(
            model_name='pimluritem',
            name='quiz',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='quiz.Quiz'),
        ),
        migrations.AlterUniqueTogether(
            name='pimluruser',
            unique_together={('user', 'pimlur')},
        ),
    ]
