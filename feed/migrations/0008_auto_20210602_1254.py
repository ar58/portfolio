# Generated by Django 3.1.2 on 2021-06-02 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0007_auto_20210602_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intro',
            name='fb',
            field=models.CharField(default='https://www.facebook.com/ar58p/', max_length=264),
        ),
        migrations.AlterField(
            model_name='intro',
            name='github',
            field=models.CharField(default='https://github.com/ar58', max_length=264),
        ),
        migrations.AlterField(
            model_name='intro',
            name='linked_in',
            field=models.CharField(default='https://www.linkedin.com/in/arindam-paul-314165120/', max_length=264),
        ),
        migrations.AlterField(
            model_name='intro',
            name='profession',
            field=models.CharField(default='Web Developer', max_length=160),
        ),
    ]
