# Generated by Django 3.1.2 on 2021-06-02 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0006_auto_20210602_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='text',
            field=models.TextField(default=' '),
        ),
        migrations.AlterField(
            model_name='intro',
            name='fb',
            field=models.CharField(max_length=264),
        ),
        migrations.AlterField(
            model_name='intro',
            name='github',
            field=models.CharField(max_length=264),
        ),
        migrations.AlterField(
            model_name='intro',
            name='linked_in',
            field=models.CharField(max_length=264),
        ),
        migrations.AlterField(
            model_name='intro',
            name='profession',
            field=models.CharField(max_length=160),
        ),
    ]
