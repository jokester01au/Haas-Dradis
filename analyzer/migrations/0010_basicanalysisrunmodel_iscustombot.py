# Generated by Django 2.0.7 on 2018-07-30 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyzer', '0009_auto_20180729_2050'),
    ]

    operations = [
        migrations.AddField(
            model_name='basicanalysisrunmodel',
            name='isCustomBot',
            field=models.BooleanField(default=False),
        ),
    ]
