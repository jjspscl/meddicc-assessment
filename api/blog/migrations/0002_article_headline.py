# Generated by Django 5.0.4 on 2024-04-28 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='headline',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
