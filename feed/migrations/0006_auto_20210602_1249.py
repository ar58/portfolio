# Generated by Django 3.1.2 on 2021-06-02 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0005_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='text',
            field=models.TextField(default='-'),
        ),
    ]
