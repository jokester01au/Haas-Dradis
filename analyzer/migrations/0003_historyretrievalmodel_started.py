# Generated by Django 2.0.7 on 2018-07-29 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyzer', '0002_historyretrievalmodel_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='historyretrievalmodel',
            name='started',
            field=models.BooleanField(default=False),
        ),
    ]
